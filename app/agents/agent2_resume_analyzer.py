import json

from app.llm import ask_llm
from app.models.candidate import CandidateProfile
from app.utils.document_parser import extract_resume_text


SYSTEM_PROMPT = """
You are a Resume Analysis Agent.

Your task is to analyze a candidate's resume and convert it into
a structured candidate profile.

Extract ONLY information explicitly supported by the resume.

Do NOT invent:

- skills
- technologies
- responsibilities
- achievements
- job titles
- companies
- projects
- certifications
- education
- years of experience

If information is not available, use an empty string or empty list.

Extract:

1. Candidate name
2. Total experience
3. Skills
4. Work experience
5. Technologies used
6. Projects
7. Education
8. Certifications

Return ONLY valid JSON.

Use exactly this structure:

{
    "name": "",
    "total_experience": "",
    "skills": [],
    "experiences": [
        {
            "company": "",
            "role": "",
            "duration": "",
            "responsibilities": [],
            "technologies": []
        }
    ],
    "projects": [
        {
            "name": "",
            "description": "",
            "technologies": []
        }
    ],
    "education": [],
    "certifications": []
}
"""


def analyze_resume(file_path: str) -> CandidateProfile:
    """Parse and analyze a candidate resume."""

    resume_text = extract_resume_text(file_path)

    prompt = f"""
{SYSTEM_PROMPT}

CANDIDATE RESUME
----------------
{resume_text}
----------------

Return ONLY valid JSON.
"""

    response = ask_llm(prompt).strip()

    # Handle accidental markdown code fences.
    if response.startswith("```"):
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()


    data = json.loads(response)

    return CandidateProfile.model_validate(data)