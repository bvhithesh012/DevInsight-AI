from app.services.github.github_client import get_github_profile


def analyze_profile(username: str):

    profile = get_github_profile(username)

    if not profile:
        return None

    return {
        "username": profile.get("login"),
        "name": profile.get("name"),
        "bio": profile.get("bio"),
        "public_repos": profile.get("public_repos"),
        "followers": profile.get("followers"),
        "following": profile.get("following"),
        "profile_url": profile.get("html_url"),
        "avatar_url": profile.get("avatar_url"),
        "created_at": profile.get("created_at"),
    }