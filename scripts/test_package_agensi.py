"""Regression checks for the marketplace archive boundary."""
import contextlib
import io
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

import package_agensi as package


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        for source in [*package.FILES.values(), ".claude-plugin/plugin.json"]:
            dest = self.root / source
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(package.ROOT / source, dest)
        self.out = Path(self.temp.name) / "dist"
        self.addCleanup(patch.stopall)
        patch.object(package, "ROOT", self.root).start()

    def build(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return package.build(self.out)

    def test_reproducible_allowlist_excludes_repository_material(self):
        (self.root / "private-plan.md").write_text("not skill content", encoding="utf-8")
        first = self.build().read_bytes()
        archive = self.build()
        self.assertEqual(first, archive.read_bytes())
        with ZipFile(archive) as bundle:
            self.assertEqual(set(bundle.namelist()), set(package.FILES))
            self.assertEqual(len(bundle.namelist()), 6)
            self.assertIsNone(bundle.testzip())

    def test_missing_reference_rejects_package(self):
        skill = self.root / "skills/lux-swiss/SKILL.md"
        with skill.open("a", encoding="utf-8") as stream:
            stream.write("\n[Missing](references/missing.md)\n")
        with self.assertRaisesRegex(ValueError, "Unresolved local reference"):
            self.build()

    def test_credential_shaped_content_rejects_package(self):
        theme = self.root / "skills/lux-swiss/assets/theme.css"
        with theme.open("a", encoding="utf-8") as stream:
            stream.write("\n/* " + "ghp_" + "X" * 36 + " */\n")
        with self.assertRaisesRegex(ValueError, "Credential-shaped material"):
            self.build()


if __name__ == "__main__":
    unittest.main()
