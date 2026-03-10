"""Requirement schema (Week 1 - requirement parser output)."""

from pydantic import BaseModel, Field


class RequirementSummary(BaseModel):
    """Normalized requirement from free-text input."""

    feature_name: str = Field(..., description="Name of the feature")
    actors: list[str] = Field(default_factory=list, description="User roles or actors")
    happy_path: list[str] = Field(default_factory=list, description="Main success flow steps")
    error_paths: list[str] = Field(default_factory=list, description="Error/edge scenarios")
    assumptions: list[str] = Field(default_factory=list, description="Preconditions or assumptions")
