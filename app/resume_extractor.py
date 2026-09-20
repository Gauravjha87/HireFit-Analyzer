from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv

from resume_schema import ResumeSchema


load_dotenv()

llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

structured_llm = llm.with_structured_output(Resume)


def extract_resume_data(resume_text):
    prompt = f"""
    Extract structured information from the following resume.

    resume:
    {resume_text}


    Extract:
    - candidate name
    - skills
    - work experience
    - education
    - projects
    - certifications

    Return only information that is present in the resume.
    Do not invent information

"""
    result = structured_llm.invoke(prompt)
    return result
    
    




