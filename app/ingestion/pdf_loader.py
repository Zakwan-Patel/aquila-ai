from pathlib import Path
from typing import List
from langchain_core.documents import Document
from pypdf import PdfReader


def load_pdf(pdf_path: str) -> List[Document]:
    """
    Load a PDF and return LangChain Document objects
    with metadata attached.
    """
    pdf_path = Path(pdf_path)
    reader = PdfReader(pdf_path)

    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if not text:
            continue

        doc = Document(
            page_content=text,
            metadata={
                "source": pdf_path.name,
                "page": page_number + 1
            }
        )

        documents.append(doc)

    return documents
