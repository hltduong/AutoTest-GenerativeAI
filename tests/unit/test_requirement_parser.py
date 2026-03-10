"""Tests for requirement parser (Week 2 deliverable)."""

import pytest

from src.models.requirement import RequirementSummary
from src.parsers.requirement_parser import parse_requirement


def test_parse_valid_requirement() -> None:
    """Valid input produces RequirementSummary."""
    text = "User Login\nUser enters email\nUser enters password\nUser clicks Login"
    result = parse_requirement(text)
    assert result.feature_name == "User Login"
    assert len(result.happy_path) == 3


def test_parse_empty_produces_unnamed() -> None:
    """Empty input produces Unnamed feature."""
    result = parse_requirement("")
    assert result.feature_name == "Unnamed"
    assert result.happy_path == []


def test_parse_single_line() -> None:
    """Single line is feature name only."""
    result = parse_requirement("Feature X")
    assert result.feature_name == "Feature X"
    assert result.happy_path == []
