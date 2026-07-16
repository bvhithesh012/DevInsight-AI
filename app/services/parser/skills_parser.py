import re

SKILL_DATABASE = [

    "Python",
    "FastAPI",
    "Flask",
    "Django",

    "SQL",
    "MySQL",
    "PostgreSQL",
    "Supabase",
    "MongoDB",

    "REST API",
    "REST APIs",
    "CRUD",

    "Git",
    "GitHub",
    "Docker",
    "Postman",
    "VS Code",

    "Pandas",
    "NumPy",
    "OpenCV",

    "Java",
    "JavaScript",
    "TypeScript",
    "React",

    "HTML",
    "CSS",

    "OOP",
    "DBMS"
]


def extract_skills(text):

    skills = []

    for skill in SKILL_DATABASE:

        if re.search(re.escape(skill), text, re.IGNORECASE):
            skills.append(skill)

    return sorted(list(set(skills)))