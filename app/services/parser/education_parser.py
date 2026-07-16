import re


def extract_education(text: str):

    education = []

    patterns = [
        r'B\.?Tech.*?(?=\n\n|\n[A-Z ]{3,}|$)',
        r'Bachelor.*?(?=\n\n|\n[A-Z ]{3,}|$)',
        r'Intermediate.*?(?=\n\n|\n[A-Z ]{3,}|$)',
        r'Secondary.*?(?=\n\n|\n[A-Z ]{3,}|$)'
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        education.extend(matches)

    return education