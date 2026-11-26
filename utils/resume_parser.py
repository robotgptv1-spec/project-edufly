
import pdfplumber
from docx import Document
import os


def extract_pdf_text(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()


def extract_docx_text(file_path):

    doc = Document(file_path)

    text = []

    for paragraph in doc.paragraphs:

        if paragraph.text.strip():
            text.append(paragraph.text.strip())

    return "\n".join(text)


def parse_resume(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found")

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format")
