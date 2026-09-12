import json

from app.llm import ask_llm
from app.models.candidate import CandidateProfile
from app.models.gap_analysis import GapAnalysis
from app.models.job import JobProfile


SYSTEM_PROMPT = """
You are a Resume-to-Job Gap Analysis Agent.

Your job is to compare a structured job profile against a structured
candidate profile.

The goal is to identify how well the candidate matches the job and
what legitimate resume improvements could be made.

IMPORTANT RULE:

NEVER invent candidate experience.

Only treat something as a candidate skill or experience if it is
supported by the candidate profile.

Classify requirements into:

1. strong_matches
   Requirements clearly supported by the candidate's experience,
   skills, projects, or technologies.

2. partial_matches
   Requirements where the candidate has related or transferable
   experience but does not clearly demonstrate the exact requirement.

3. genuine_gaps
   Requirements that are explicitly requested by the job but are not
   supported by the candidate profile.

4. recommended_changes
   Legitimate changes that could improve the resume using information
   already present in the candidate profile.

5. fabrication_risks
   Requirements that would require inventing experience, skills,
   technologies, achievements, or responsibilities.

RULES:
1. A skill can be classified as a strong match ONLY if it is explicitly
supported by the candidate profile.
2. A skill can be classified as a partial match ONLY if:
- the candidate profile contains clearly related experience, AND
- the relationship is defensible from the provided evidence.
3. Do NOT classify a skill as partial merely because it is commonly used
with another skill.
For example:
Python does NOT imply Django.
Python does NOT imply FastAPI.
Azure does NOT imply AWS.
LLM experience does NOT imply React.
Git knowledge must be explicitly supported.

4.If there is insufficient evidence, classify it as a genuine gap.

Scoring:

Give an overall match score from 0 to 100.

Use this approximate weighting:

- Skills match: 35%
- Experience match: 25%
- Keyword coverage: 15%
- Responsibility match: 15%
- Education: 10%

The score should be an analytical estimate, NOT a claim that it
replicates a proprietary ATS.

For every recommendation, provide evidence from the candidate profile.

Return ONLY valid JSON.

Use exactly this structure:

{
    "overall_match_score": 0,
    "strong_matches": [],
    "partial_matches": [],
    "genuine_gaps": [],
    "recommended_changes": [
        {
            "target": "",
            "recommendation": "",
            "evidence": ""
        }
    ],
    "fabrication_risks": []
}
"""


def analyze_gap(
    job_profile: JobProfile,
    candidate_profile: CandidateProfile,
) -> GapAnalysis:

    prompt = f"""
{SYSTEM_PROMPT}

JOB PROFILE
-----------

{job_profile.model_dump_json(indent=2)}

CANDIDATE PROFILE
-----------------

{candidate_profile.model_dump_json(indent=2)}

Compare the candidate against the job.

Return ONLY valid JSON.
"""

    response = ask_llm(prompt).strip()

    if response.startswith("```"):
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

    print("\n===== GAP ANALYSIS RESPONSE =====")
    print(response)
    data = json.loads(response)

    return GapAnalysis.model_validate(data)