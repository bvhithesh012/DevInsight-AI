def compare_skills(resume_skills: list, github_skills: list):

    resume_set = {skill.lower() for skill in resume_skills}
    github_set = {skill.lower() for skill in github_skills}

    matching_skills = sorted(resume_set & github_set)
    resume_only = sorted(resume_set - github_set)
    github_only = sorted(github_set - resume_set)

    return {
        "matching_skills": matching_skills,
        "resume_only_skills": resume_only,
        "github_only_skills": github_only,
        "match_percentage": (
            round((len(matching_skills) / len(resume_set)) * 100, 2)
            if resume_set else 0
        )
    }