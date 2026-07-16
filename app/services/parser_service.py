import fitz


def extract_pdf_text(file_path: str):

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


import re


def parse_resume(text: str):

    skills = []

    skill_keywords = [
        "Python",
        "FastAPI",
        "Django",
        "Flask",
        "SQL",
        "PostgreSQL",
        "MongoDB",
        "Docker",
        "Git",
        "React",
        "Java",
        "C",
        "C++",
        "JavaScript"
    ]

    for skill in skill_keywords:
        if re.search(skill, text, re.IGNORECASE):
            skills.append(skill)

    return {
        "skills": skills,
        "raw_text": text
    }