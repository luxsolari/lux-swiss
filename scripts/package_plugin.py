#!/usr/bin/env python3
"""Build the public native-plugin ZIP, preserving its installation layout."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent.parent


def build(output_dir: Path) -> Path:
    manifest_path = ".claude-plugin/plugin.json"
    manifest = json.loads((ROOT / manifest_path).read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Invalid plugin name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Plugin version must be strict semver")
    if manifest.get("skills") != "./skills/":
        raise ValueError("Unexpected skill installation path")
    files = [manifest_path, f"skills/{name}/SKILL.md",
             f"skills/{name}/assets/theme.css", f"skills/{name}/references/components.md",
             "HOUSE-MARK.md", "LICENSE", "LICENSE-DESIGN"]
    contents = {file: (ROOT / file).read_bytes() for file in files}
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{name}-plugin-{version}.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for file, data in sorted(contents.items()):
            info = ZipInfo(file, date_time=(2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data)
    with ZipFile(archive) as bundle:
        if set(bundle.namelist()) != set(files) or bundle.testzip() is not None:
            raise ValueError("Plugin archive integrity or allowlist check failed")
        for file, data in contents.items():
            if bundle.read(file) != data:
                raise ValueError(f"Payload mismatch: {file}")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"{archive}: {len(files)} files, {archive.stat().st_size} bytes")
    return archive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    build(parser.parse_args().output_dir)
