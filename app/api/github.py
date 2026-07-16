from fastapi import APIRouter, HTTPException

from app.schemas.github import GitHubProfileRequest
from app.services.github.profile_analyzer import analyze_profile
from app.services.github.repo_analyzer import analyze_repositories

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