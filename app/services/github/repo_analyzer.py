from app.services.github.github_client import (
    get_user_repositories,
    get_repository_readme
)
from app.services.github.scoring import calculate_github_score


def analyze_repositories(username: str):

    repos = get_user_repositories(username)

    if not repos:
        return {
            "github_score": 0,
            "total_repositories": 0,
            "total_stars": 0,
            "total_forks": 0,
            "primary_language": None,
            "language_distribution": {},
            "ai_projects": 0,
            "backend_projects": 0,
            "frontend_projects": 0,
            "repositories": []
        }

    repository_list = []
    language_count = {}

    total_stars = 0
    total_forks = 0

    ai_projects = 0
    backend_projects = 0
    frontend_projects = 0

    for repo in repos:

        total_stars += repo["stargazers_count"]
        total_forks += repo["forks_count"]

        # Count languages
        language = repo["language"]
        if language:
            language_count[language] = language_count.get(language, 0) + 1

        # Search repository name + description
        #readme = get_repository_readme(username, repo["name"])
        repo_name = repo["name"].lower()
        repo_description = (repo.get("description") or "").lower()
        search_text = f"{repo_name} {repo_description}"

        # AI/ML Projects
        if any(keyword in search_text for keyword in [
            "ai",
            "ml",
            "machine learning",
            "deep learning",
            "neural",
            "llm",
            "openai",
            "gemini"
        ]):
            ai_projects += 1

        # Backend Projects
        if any(keyword in search_text for keyword in [
            "api",
            "backend",
            "server",
            "fastapi",
            "flask",
            "django",
            "spring"
        ]):
            backend_projects += 1

        # Frontend Projects
        if any(keyword in search_text for keyword in [
            "frontend",
            "react",
            "vue",
            "angular",
            "ui",
            "nextjs",
            "next.js"
        ]):
            frontend_projects += 1

        repository_list.append({
          "name": repo["name"],
          "language": language,
          "stars": repo["stargazers_count"],
          "forks": repo["forks_count"],
          "size_kb": repo["size"],
          "default_branch": repo["default_branch"],
          "private": repo["private"],
          "url": repo["html_url"],
          "topics": repo.get("topics", []),
          "has_readme": None,
          "readme_length": None,
        })

    # Primary language
    primary_language = None
    if language_count:
        primary_language = max(language_count, key=language_count.get)

    # Statistics for scoring
    stats = {
        "total_repositories": len(repository_list),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "language_distribution": language_count,
        "ai_projects": ai_projects,
        "backend_projects": backend_projects,
        "frontend_projects": frontend_projects
    }

    github_score = calculate_github_score(stats)

    return {
        "github_score": github_score,
        "total_repositories": len(repository_list),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "primary_language": primary_language,
        "language_distribution": language_count,
        "ai_projects": ai_projects,
        "backend_projects": backend_projects,
        "frontend_projects": frontend_projects,
        "repositories": repository_list
    }