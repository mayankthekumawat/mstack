"""Copy mstack skills into agent skill directories, preserving local edits."""

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def inventory():
    skills = {}
    for collection in (ROOT / "pstack/skills", ROOT / "skills"):
        if collection.is_dir():
            for source in sorted(collection.iterdir()):
                if (source / "SKILL.md").is_file():
                    if source.name in skills:
                        raise ValueError(f"Duplicate skill name: {source.name}")
                    skills[source.name] = source
    return skills


def different_files(source, target):
    changed = []
    for path in source.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        installed = target / path.relative_to(source)
        if installed.is_symlink():
            changed.append(str(path.relative_to(source)))
        elif installed.exists() and (not installed.is_file() or
                path.read_bytes().replace(b"\r\n", b"\n") != installed.read_bytes().replace(b"\r\n", b"\n")):
            changed.append(str(path.relative_to(source)))
    return changed


def sync(skills, destination, apply):
    results = []
    destination = destination.expanduser().resolve()
    for name, source in skills.items():
        target = destination / name
        if target.is_symlink() or (target.exists() and not target.is_dir()):
            results.append({"skill": name, "status": "conflict", "files": ["skill path is not a plain directory"]})
            continue
        changed = different_files(source, target)
        if changed:
            results.append({"skill": name, "status": "conflict", "files": changed})
            continue
        missing = [p for p in source.rglob("*") if p.is_file() and "__pycache__" not in p.parts
                   and p.suffix != ".pyc" and not (target / p.relative_to(source)).exists()]
        if apply and missing:
            for path in missing:
                installed = target / path.relative_to(source)
                installed.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, installed)
        results.append({"skill": name, "status": ("installed" if apply else "would-install") if missing else "current"})
    return {"destination": str(destination), "apply": apply, "skills": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, action="append", required=True)
    parser.add_argument("--skill", action="append", help="Select a skill by name; repeat to select several. Default: all.")
    parser.add_argument("--apply", action="store_true", help="Copy missing files. Default: show the plan only.")
    args = parser.parse_args()
    skills = inventory()
    if args.skill:
        unknown = set(args.skill) - skills.keys()
        if unknown:
            parser.error(f"Unknown skills: {', '.join(sorted(unknown))}")
        skills = {name: skills[name] for name in dict.fromkeys(args.skill)}
    results = [sync(skills, destination, args.apply) for destination in args.destination]
    print(json.dumps(results, indent=2))
    if any(item["status"] == "conflict" for result in results for item in result["skills"]):
        parser.exit(2, "Local edits preserved. Reconcile the listed conflicts before claiming a full sync.\n")


if __name__ == "__main__":
    main()
