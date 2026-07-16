from app.services.parser.pdf_parser import extract_pdf_text
from app.services.parser.contact_parser import (
    extract_name,
    extract_email,
    extract_phone,
    extract_location,
)
from app.services.parser.skills_parser import extract_skills
from app.services.parser.education_parser import extract_education
from app.services.parser.experience_parser import extract_experience
from app.services.parser.project_parser import extract_projects
from app.services.parser.certification_parser import extract_certifications


def parse_resume(file_path: str):

    text = extract_pdf_text(file_path)

    return {
        "candidate": {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
            "location": extract_location(text),
        },
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "projects": extract_projects(text),
        "certifications": extract_certifications(text),
        "raw_text": text
    }