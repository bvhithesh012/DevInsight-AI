def build_candidate_profile(
    resume_data: dict,
    github_data: dict,
    skill_comparison: dict
):
    return {
        "candidate": resume_data.get("candidate"),
        "resume": resume_data,
        "github": github_data,
        "skill_comparison": skill_comparison
    }