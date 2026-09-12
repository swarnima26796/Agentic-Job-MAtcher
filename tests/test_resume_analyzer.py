from app.agents.agent2_resume_analyzer import analyze_resume


resume_path = "data/resume/Swarnima_Resume1.pdf"

candidate_profile = analyze_resume(resume_path)

print("\n===== CANDIDATE PROFILE =====")
print(candidate_profile.model_dump_json(indent=2))