import json

from app.llm import ask_llm
from app.models.job import JobProfile
from app.utils.document_parser import extract_job_text


SYSTEM_PROMPT = """
You are a Job Analysis Agent.

Your task is to analyze a job description and convert it into a
structured job profile.

Extract only information that is explicitly supported by the
job description.

Extract:

1. Job title
2. Company
3. Location
4. Experience requirements
5. Mandatory skills
6. Nice-to-have skills
7. Responsibilities
8. Important keywords
9. Education requirements

Rules:

- Do not invent requirements.
- Do not infer skills that are not mentioned.
- Keep skills concise.
- Keep responsibilities concise.
- Important keywords should capture technologies, methodologies,
  role-specific terminology, and important phrases from the JD.

Return ONLY valid JSON.

Use exactly this structure:

{
    "job_title": "",
    "company": "",
    "location": "",
    "experience_required": "",
    "must_have_skills": [],
    "nice_to_have_skills": [],
    "responsibilities": [],
    "keywords": [],
    "education_requirements": []
}
"""


def analyze_job(file_path: str) -> JobProfile:
    """Parse and analyze a job description."""

    job_text = extract_job_text(file_path)

    prompt = f"""
{SYSTEM_PROMPT}

JOB DESCRIPTION
---------------
{job_text}
---------------

Return ONLY valid JSON.
"""

    response = ask_llm(prompt).strip()

    # Handle accidental markdown code fences.
    if response.startswith("```"):
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

    data = json.loads(response)

    return JobProfile.model_validate(data)