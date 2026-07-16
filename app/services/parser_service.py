import fitz
import re


def extract_pdf_text(file_path: str):
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else ""


def extract_phone(text):
    match = re.search(r'(\+91[-\s]?)?[6-9]\d{9}', text)
    return match.group(0) if match else ""


def extract_name(text):
    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if len(line) > 3 and line.isupper():
            return line

    return ""


def extract_location(text):
    match = re.search(
        r'([A-Za-z ]+,\s*[A-Za-z ]+)',
        text
    )

    return match.group(0) if match else ""


def parse_resume(text):

    skills = []

    skill_keywords = [
        "Python",
        "FastAPI",
        "Flask",
        "Django",
        "REST API",
        "REST APIs",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "Supabase",
        "MongoDB",
        "Docker",
        "Git",
        "GitHub",
        "Postman",
        "VS Code",
        "Pandas",
        "NumPy",
        "OpenCV",
        "React",
        "Java",
        "JavaScript",
        "HTML",
        "CSS",
        "OOP",
        "DBMS",
        "CRUD"
    ]

    for skill in skill_keywords:
        if re.search(re.escape(skill), text, re.IGNORECASE):
            skills.append(skill)

    return {
        "candidate": {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
            "location": extract_location(text)
        },
        "skills": sorted(list(set(skills))),
        "raw_text": text
    }