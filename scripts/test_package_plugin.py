"""Check the public artifact's native layout and packaging boundary."""
import contextlib
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

import package_plugin as package


class PluginTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        for file in (".claude-plugin/plugin.json", "HOUSE-MARK.md", "LICENSE", "LICENSE-DESIGN"):
            dest = self.root / file
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(package.ROOT / file, dest)
        shutil.copytree(package.ROOT / "skills", self.root / "skills")
        self.name = json.loads((self.root / ".claude-plugin/plugin.json").read_text())["name"]
        self.out = Path(self.temp.name) / "dist"
        self.addCleanup(patch.stopall)
        patch.object(package, "ROOT", self.root).start()

    def build(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return package.build(self.out)

    def test_native_layout_reproducibility_and_exclusions(self):
        (self.root / "private-plan.md").write_text("Not plugin content")
        first = self.build().read_bytes()
        archive = self.build()
        self.assertEqual(first, archive.read_bytes())
        with ZipFile(archive) as bundle:
            self.assertEqual(len(bundle.namelist()), 7)
            self.assertIn(".claude-plugin/plugin.json", bundle.namelist())
            self.assertIn(f"skills/{self.name}/SKILL.md", bundle.namelist())
            self.assertNotIn("SKILL.md", bundle.namelist())
            for file in bundle.namelist():
                self.assertEqual(bundle.read(file), (self.root / file).read_bytes())

    def test_missing_theme_rejected(self):
        (self.root / f"skills/{self.name}/assets/theme.css").unlink()
        with self.assertRaises(FileNotFoundError):
            self.build()

    def test_unexpected_skill_path_rejected(self):
        file = self.root / ".claude-plugin/plugin.json"
        manifest = json.loads(file.read_text())
        manifest["skills"] = "../outside/"
        file.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "installation path"):
            self.build()


if __name__ == "__main__":
    unittest.main()
