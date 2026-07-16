import re


def extract_name(text):

    for line in text.splitlines():

        line = line.strip()

        if len(line) > 3 and line.isupper():
            return line

    return ""


def extract_email(text):

    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    return match.group(0) if match else ""


def extract_phone(text):

    match = re.search(r'(\+91[-\s]?)?[6-9]\d{9}', text)

    return match.group(0) if match else ""


def extract_location(text):

    match = re.search(r'([A-Za-z ]+,\s*[A-Za-z ]+)', text)

    return match.group(0) if match else ""