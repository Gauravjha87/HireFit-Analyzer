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
