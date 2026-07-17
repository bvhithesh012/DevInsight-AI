from pydantic import BaseModel, HttpUrl


class GitHubProfileRequest(BaseModel):
    github_url: HttpUrl
    
class GitHubReadmeRequest(BaseModel):
    github_url: HttpUrl
    repository_name: str    
    
class SkillComparisonRequest(BaseModel):
    resume_skills: list[str]
    github_skills: list[str]    
 
class CandidateProfileRequest(BaseModel):
    github_url: HttpUrl
    resume_skills: list[str]    
    
class CandidateProfileRequest(BaseModel):
    github_url: HttpUrl
    resume_data: dict    