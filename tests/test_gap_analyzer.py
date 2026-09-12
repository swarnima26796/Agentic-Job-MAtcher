from app.agents.agent1_job_analyzer import analyze_job
from app.agents.agent2_resume_analyzer import analyze_resume
from app.agents.agent3_gap_analyzer import analyze_gap


job_path = "data/jobs/Bain & Company.txt"
resume_path = "data/resume/Swarnima_Resume1.pdf"


job_profile = analyze_job(job_path)

candidate_profile = analyze_resume(resume_path)

gap_analysis = analyze_gap(
    job_profile=job_profile,
    candidate_profile=candidate_profile,
)


print("\n===== GAP ANALYSIS =====")
print(gap_analysis.model_dump_json(indent=2))