from app.agents.agent1_job_analyzer import analyze_job


job_path = "data/jobs/Bain & Company.txt"

job_profile = analyze_job(job_path)

print("\n===== JOB PROFILE =====")
print(job_profile.model_dump_json(indent=2))