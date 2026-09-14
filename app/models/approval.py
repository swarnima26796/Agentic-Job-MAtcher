from typing import List

from pydantic import BaseModel, Field


class ApprovedChange(BaseModel):
    target: str = ""
    recommendation: str = ""
    evidence: str = ""
    decision: str = ""


class ApprovalResult(BaseModel):
    changes: List[ApprovedChange] = Field(default_factory=list)