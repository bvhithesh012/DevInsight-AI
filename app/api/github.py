from fastapi import APIRouter, HTTPException

from app.schemas.github import (
    GitHubProfileRequest,
    GitHubReadmeRequest,
    SkillComparisonRequest,
)
from app.schemas.github import CandidateProfileRequest
from app.services.profile_analyzer import build_candidate_profile
from app.services.github.profile_analyzer import analyze_profile
from app.services.github.repo_analyzer import analyze_repositories
from app.services.github.github_client import get_repository_readme
from app.services.github.readme_analyzer import analyze_readme


from app.services.skill_comparison import compare_skills

router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)


@router.post("/profile")
def github_profile(request: GitHubProfileRequest):

    github_url = str(request.github_url)
    username = github_url.rstrip("/").split("/")[-1]

    result = analyze_profile(username)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="GitHub profile not found"
        )

    return result


@router.post("/repositories")
def github_repositories(request: GitHubProfileRequest):

    github_url = str(request.github_url)
    username = github_url.rstrip("/").split("/")[-1]

    repositories = analyze_repositories(username)

    return {
        "username": username,
        "repositories": repositories
    }


@router.post("/readme")
def github_readme(request: GitHubReadmeRequest):

    github_url = str(request.github_url)
    username = github_url.rstrip("/").split("/")[-1]

    readme = get_repository_readme(
        username,
        request.repository_name
    )

    if not readme:
        raise HTTPException(
            status_code=404,
            detail="README not found"
        )

    analysis = analyze_readme(readme)

    return {
        "repository": request.repository_name,
        "analysis": analysis,
        "readme": readme
    }


@router.post("/compare-skills")
def compare_resume_github_skills(request: SkillComparisonRequest):

    result = compare_skills(
        request.resume_skills,
        request.github_skills
    )

    return result
@router.post("/candidate-profile")
def candidate_profile(request: CandidateProfileRequest):

    github_url = str(request.github_url)
    username = github_url.rstrip("/").split("/")[-1]

    github_profile = analyze_profile(username)

    if not github_profile:
        raise HTTPException(
            status_code=404,
            detail="GitHub profile not found"
        )

    github_repositories = analyze_repositories(username)

    github_data = {
        "profile": github_profile,
        "repositories": github_repositories
    }

    github_skills = list(
    github_repositories.get("language_distribution", {}).keys()
   )
    resume = request.resume_data.get("parsed_data", {})

    resume_skills = resume.get("skills", [])

    skill_comparison = compare_skills(
        resume_skills,
        github_skills
    )

    profile = build_candidate_profile(
        resume_data=resume,
        github_data=github_data,
        skill_comparison=skill_comparison
    )

    return profile