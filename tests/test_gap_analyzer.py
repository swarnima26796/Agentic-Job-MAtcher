from app.agents.agent1_job_analyzer import analyze_job
from app.agents.agent2_resume_analyzer import analyze_resume
from app.agents.agent3_gap_analyzer import analyze_gap
from app.agents.human_approval import get_human_approval
from app.utils.audit_logger import save_audit_log

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

approval_result = get_human_approval(gap_analysis)

print("\n===== APPROVAL RESULT =====")
print(approval_result.model_dump_json(indent=2))

print("\n===== APPROVAL RESULT =====")
print(approval_result.model_dump_json(indent=2))
save_audit_log(approval_result)
