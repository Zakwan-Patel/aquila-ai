import re


def clean_text(text: str) -> str:
    if not text:
        return ""

    # Replace tabs and multiple spaces with single space
    text = re.sub(r"\s+", " ", text)

    # Remove weird unicode leftovers
    text = text.replace("\u00a0", " ")

    # Strip leading/trailing whitespace
    text = text.strip()

    return text
