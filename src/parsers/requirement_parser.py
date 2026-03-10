"""CLI script: requirement text -> normalized JSON (Week 1 deliverable)."""

import json
import sys
from pathlib import Path

from src.models.requirement import RequirementSummary


def parse_requirement(text: str) -> RequirementSummary:
    """Parse free-text requirement into normalized JSON."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    # Simple heuristic: first line = feature name, rest = steps/assumptions
    feature_name = lines[0] if lines else "Unnamed"
    steps = lines[1:] if len(lines) > 1 else []
    return RequirementSummary(
        feature_name=feature_name,
        actors=[],
        happy_path=steps,
        error_paths=[],
        assumptions=[],
    )


def main() -> int:
    """CLI: accepts requirement text file, outputs JSON."""
    if len(sys.argv) < 2:
        print("Usage: python -m src.parsers.requirement_parser <requirement.txt>")
        return 1
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 1
    text = path.read_text(encoding="utf-8")
    summary = parse_requirement(text)
    print(json.dumps(summary.model_dump(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
