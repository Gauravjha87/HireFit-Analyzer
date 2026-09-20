from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def generate_interview_questions(resume_text, job_description_text, missed_skills):

    prompt = f"""
    Generate a set of interview questions based on the following resume, job description, and missed skills. 
    
    resume_text:
    {resume_text}

    job_description_text:
    {job_description_text}

    missed_skills:
    {missed_skills}

    Generate interview questions in the following categories:

1. RESUME-BASED QUESTIONS
   Ask questions about the candidate's projects,
   skills, experience, and technologies mentioned
   in the resume.

2. JD TECHNICAL QUESTIONS
   Ask technical questions based on the important
   technologies and skills required by the JD.

3. SKILL-GAP QUESTIONS
   Ask questions about skills identified as missing
   or partially matched.

4. SCENARIO-BASED QUESTIONS
   Ask practical questions related to the responsibilities
   described in the JD.


   Do not ask irrelevant questions.

Do not assume that the candidate has experience
that is not present in the resume.

Generate approximately 5 questions per category.
    """

    response = llm.invoke(prompt)
    return response.content
