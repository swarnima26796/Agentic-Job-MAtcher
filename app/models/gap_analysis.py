from typing import List

from pydantic import BaseModel, Field


class Recommendation(BaseModel):
    target: str = ""
    recommendation: str = ""
    evidence: str = ""


class GapAnalysis(BaseModel):
    overall_match_score: float = 0.0

    strong_matches: List[str] = Field(default_factory=list)
    partial_matches: List[str] = Field(default_factory=list)
    genuine_gaps: List[str] = Field(default_factory=list)

    recommended_changes: List[Recommendation] = Field(
        default_factory=list
    )

    fabrication_risks: List[str] = Field(default_factory=list)