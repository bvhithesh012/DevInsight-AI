from app.services.github.github_client import get_user_repositories


def analyze_repositories(username: str):

    repos = get_user_repositories(username)

    if not repos:
        return []

    repository_list = []

    for repo in repos:

        repository_list.append({
            "name": repo["name"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "private": repo["private"],
            "url": repo["html_url"]
        })

    return repository_list