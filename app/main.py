from pydoc import text

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from resume_parser import extract_text_from_pdf
from skill_matcher import match_skills
from interview_question_generator import generate_interview_questions
from embedding import create_resume_vectorstore, search_resume

resume_file_path =  r"C:\Documents\AI-Powered Resume Analyzer\resume.pdf"
#print("PDF PATH: ", resume_file_path)
resume_text = extract_text_from_pdf(resume_file_path)


with open(r"C:\Documents\AI-Powered Resume Analyzer\job_des.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

matched_skills = match_skills(resume_text, jd_text)
print("RESUME vs JD ANALYSIS: ")
print(matched_skills)

interview_questions = generate_interview_questions(resume_text, jd_text, matched_skills)
print("INTERVIEW QUESTIONS: ")
print(interview_questions)

vectorstore = create_resume_vectorstore(resume_file_path)
print("\n========== VECTOR STORE ==========\n")
print("Resume successfully embedded and stored in Chroma.")

jd_requirement = """
Strong exposure in prompt engineering,
knowledge of vector database, LangChain framework
and data embeddings.
"""

results = search_resume(
    vectorstore,
    jd_requirement,
    k=3
)

print("\n========== SEMANTIC SEARCH RESULTS ==========\n")

for i, doc in enumerate(results, start=1):

    print(f"\n--- Result {i} ---")

    print(doc.page_content)