from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()


# -------------------------
# Document Loading
# -------------------------

def document_process(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()


    # -------------------------
    # Text Splitting
    # -------------------------

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = text_splitter.split_documents(docs)

    return docs


# -------------------------
# Embedding Model
# -------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)


# -------------------------
# Create Resume Vector Store
# -------------------------

def create_resume_vectorstore(pdf_path):

    resume_documents = document_process(pdf_path)

    vectorstore = Chroma.from_documents(
        documents=resume_documents,
        embedding=embeddings,
        collection_name="resume",
        persist_directory="./chroma_db"
    )

    return vectorstore

# -----------------------------
# Search Resume
# -----------------------------

def search_resume(vectorstore, jd_requirement, k=3):

    results = vectorstore.similarity_search(
        jd_requirement,
        k=k
    )

    return results