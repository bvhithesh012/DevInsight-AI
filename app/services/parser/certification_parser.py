import re


def extract_certifications(text: str):

    certifications = []

    section_pattern = r'CERTIFICATIONS(.*?)(?=ADDITIONAL INFORMATION|$)'

    match = re.search(
        section_pattern,
        text,
        re.DOTALL | re.IGNORECASE
    )

    if not match:
        return certifications

    cert_section = match.group(1)

    lines = [
        line.strip()
        for line in cert_section.splitlines()
        if line.strip()
    ]

    for line in lines:
        certifications.append(line)

    return certifications