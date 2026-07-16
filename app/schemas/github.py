from pydantic import BaseModel, HttpUrl


class GitHubProfileRequest(BaseModel):
    github_url: HttpUrl