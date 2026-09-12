from typing import List

from pydantic import BaseModel, Field


class JobProfile(BaseModel):
    job_title: str = ""
    company: str = ""
    location: str = ""
    experience_required: str = ""

    must_have_skills: List[str] = Field(default_factory=list)
    nice_to_have_skills: List[str] = Field(default_factory=list)

    responsibilities: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)

    education_requirements: List[str] = Field(default_factory=list)