from typing import List

from pydantic import BaseModel, Field


class Experience(BaseModel):
    company: str = ""
    role: str = ""
    duration: str = ""
    responsibilities: List[str] = Field(default_factory=list)
    technologies: List[str] = Field(default_factory=list)


class Project(BaseModel):
    name: str = ""
    description: str = ""
    technologies: List[str] = Field(default_factory=list)

class Education(BaseModel):
    degree: str = ""
    field: str = ""
    institution: str = ""
    specialization: str = ""
    cgpa: str = ""
    duration: str = ""


class CandidateProfile(BaseModel):
    name: str = ""
    total_experience: str = ""

    skills: List[str] = Field(default_factory=list)

    experiences: List[Experience] = Field(default_factory=list)

    projects: List[Project] = Field(default_factory=list)


    certifications: List[str] = Field(default_factory=list)