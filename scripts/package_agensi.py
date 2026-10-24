#!/usr/bin/env python3
"""Build a deterministic allowlisted skill ZIP, not a repository archive."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "SKILL.md": "skills/lux-swiss/SKILL.md",
    "assets/theme.css": "skills/lux-swiss/assets/theme.css",
    "references/components.md": "skills/lux-swiss/references/components.md",
    "HOUSE-MARK.md": "HOUSE-MARK.md",
    "LICENSE": "LICENSE",
    "LICENSE-DESIGN": "LICENSE-DESIGN",
}
SECRET_PATTERNS = {
    "GitHub token": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b",
    "AWS key": r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "Stripe key": r"\bsk_live_[A-Za-z0-9]{16,}\b",
}


def build(output_dir: Path) -> Path:
    version = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Plugin version must be strict semver")
    contents = {}
    for target, source in FILES.items():
        text = (ROOT / source).read_text(encoding="utf-8")
        if target in ("LICENSE", "LICENSE-DESIGN"):
            text = (
                "Distribution scope: SKILL.md, assets/, references/, and HOUSE-MARK.md\n"
                "are design content relocated from skills/lux-swiss/ and HOUSE-MARK.md\n"
                "in the source repository, under CC BY-SA 4.0. The original repository\n"
                "license notice follows unchanged.\n\n" + text
            )
        for label, pattern in SECRET_PATTERNS.items():
            if re.search(pattern, text):
                raise ValueError(f"Credential-shaped material ({label}) in {source}; inspect locally")
        contents[target] = text.replace("\r\n", "\n").encode("utf-8")

    frontmatter = contents["SKILL.md"].decode("utf-8").split("---", 2)[1]
    for field in ("name", "description", "tags"):
        if not re.search(rf"^{field}:\s*\S", frontmatter, re.MULTILINE):
            raise ValueError(f"Missing skill frontmatter field: {field}")
    for target, data in contents.items():
        if target.endswith(".md"):
            for link in re.findall(r"\]\(([^)]+)\)", data.decode("utf-8")):
                if link.startswith(("https://", "http://", "#")):
                    continue
                local = (Path(target).parent / link.split("#", 1)[0]).as_posix()
                if local not in contents:
                    raise ValueError(f"Unresolved local reference in {target}: {local}")

    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"lux-swiss-agensi-{version}.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for name, data in sorted(contents.items()):
            info = ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data)
    with ZipFile(archive) as bundle:
        if set(bundle.namelist()) != set(FILES) or bundle.testzip() is not None:
            raise ValueError("Archive integrity or allowlist validation failed")
        for name, data in contents.items():
            if bundle.read(name) != data:
                raise ValueError(f"Archive content mismatch: {name}")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"{archive}: {len(FILES)} files, {archive.stat().st_size} bytes")
    print(f"SHA256 {digest}")
    return archive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    build(parser.parse_args().output_dir)
