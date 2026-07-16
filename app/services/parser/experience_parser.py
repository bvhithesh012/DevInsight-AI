import re


def extract_experience(text: str):

    experience = []

    patterns = [
        r'EXPERIENCE(.*?)(?=PROJECTS|EDUCATION|CERTIFICATIONS|$)',
        r'WORK EXPERIENCE(.*?)(?=PROJECTS|EDUCATION|CERTIFICATIONS|$)',
        r'INTERNSHIP(.*?)(?=PROJECTS|EDUCATION|CERTIFICATIONS|$)'
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.DOTALL | re.IGNORECASE
        )

        if match:

            section = match.group(1)

            lines = [
                line.strip()
                for line in section.splitlines()
                if line.strip()
            ]

            experience.extend(lines)

    return experience