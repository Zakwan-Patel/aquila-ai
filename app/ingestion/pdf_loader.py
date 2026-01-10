from pypdf import PdfReader
from langchain_core.documents import Document
from app.ingestion.text_cleaner import clean_text


def load_pdf(path: str):
    reader = PdfReader(path)
    documents = []

    for page_num, page in enumerate(reader.pages):
        raw_text = page.extract_text()
        cleaned_text = clean_text(raw_text)

        # Skip empty or useless pages
        if not cleaned_text or len(cleaned_text) < 50:
            continue

        documents.append(
            Document(
                page_content=cleaned_text,
                metadata={
                    "source": path.split("/")[-1],
                    "page": page_num + 1
                }
            )
        )

    return documents
