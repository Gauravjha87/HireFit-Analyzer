from langchain_community.document_loaders import PyPDFLoader


def extract_text_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    text = ""

    for document in documents:
        text += document.page_content + "\n"

    return text