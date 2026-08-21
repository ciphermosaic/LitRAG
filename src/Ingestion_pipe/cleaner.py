import re
import unicodedata


def clean_text(text: str) -> str:
    if not text:
        return ""

    # Normalize Unicode
    text = unicodedata.normalize("NFKC", text)

    # Remove control characters, preserve \n and \t
    text = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", text)

    # Remove URLs
    text = re.sub(
        r"https?://\S+|www\.\S+",
        "",
        text
    )

    # Normalize spaces, but preserve newlines
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def clean_documents(documents):
    cleaned_documents = []

    for document in documents:
        document.page_content = clean_text(
            document.page_content
        )

        if document.page_content:
            cleaned_documents.append(document)

    return cleaned_documents