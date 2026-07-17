import base64
import requests


def get_github_profile(username: str):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def get_user_repositories(username: str):

    url = f"https://api.github.com/users/{username}/repos"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    return response.json()


def get_repository_readme(username: str, repository: str):

    url = f"https://api.github.com/repos/{username}/{repository}/readme"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()

    content = data.get("content")

    if not content:
        return None

    return base64.b64decode(content).decode("utf-8", errors="ignore")