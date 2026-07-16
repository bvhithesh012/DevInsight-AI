import re


def extract_projects(text: str):

    projects = []

    project_pattern = r'PROJECTS(.*?)(?=EDUCATION|CERTIFICATIONS|ADDITIONAL INFORMATION|$)'

    match = re.search(
        project_pattern,
        text,
        re.DOTALL | re.IGNORECASE
    )

    if not match:
        return projects

    project_section = match.group(1)

    blocks = project_section.split("Tech Stack:")

    for block in blocks:

        lines = [
            line.strip()
            for line in block.splitlines()
            if line.strip()
        ]

        if lines:
            projects.append({
                "title": lines[0],
                "details": "\n".join(lines[1:])
            })

    return projects