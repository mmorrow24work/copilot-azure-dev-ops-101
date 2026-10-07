from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
days = sorted((root / "curriculum").glob("week-*/day-*.md"))
if len(days) != 45:
    errors.append(f"Expected 45 day files, found {len(days)}")
required = ["## Purpose", "## Learning objectives", "## Azure DevOps lab", "## Validation", "## Self-check", "## Teach-back"]
for path in days:
    text = path.read_text(encoding="utf-8")
    for heading in required:
        if heading not in text:
            errors.append(f"{path.relative_to(root)} missing {heading}")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (path.parent / clean).resolve().exists():
            errors.append(f"{path.relative_to(root)} broken link {target}")

for diagram in sorted((root / "pipelines" / "diagrams").glob("*.md")):
    text = diagram.read_text(encoding="utf-8")
    if "```mermaid" not in text or "flowchart" not in text:
        errors.append(f"{diagram.relative_to(root)} missing compatible Mermaid flowchart")
if len(list((root / "pipelines" / "diagrams").glob("*.md"))) != 9:
    errors.append("Expected 9 pipeline diagram files")
if len(list((root / "labs" / "troubleshooting").glob("lab-*.md"))) != 6:
    errors.append("Expected 6 troubleshooting lab files")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: validated {len(days)} daily lessons")
