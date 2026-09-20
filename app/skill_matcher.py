from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def match_skills(resume_skills, job_description_skills):
    prompt = f"""
    compare the following skills from a resume and job description and return a list of matching skills

resume skills:
{resume_skills}

job description skills:
{job_description_skills}


Analyze the technical and professional skills required by the JD against the skills and experience present in the resume.

Categorize the skills into:

1. MATCHED SKILLS
   Skills clearly present in the resume and required by the JD.

2. PARTIALLY MATCHED SKILLS
   Skills where the candidate has related or basic knowledge,
   but the resume does not strongly demonstrate the exact JD requirement.

3. MISSING SKILLS
   Skills required by the JD that are not present in the resume.

4. MATCHING DETAILS
   Explain briefly why the matched skills are considered a match.

5. RECOMMENDATIONS
   Suggest what the candidate should learn or improve based on
   the missing and partially matched skills.

    
    """

    response = llm.invoke(prompt)
    return response.content