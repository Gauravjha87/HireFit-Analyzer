from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv

from jd_schema import JobDescriptionSchema

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

structured_llm = llm.with_structured_output(JobDescriptionSchema)

def extract_job_description_data(job_description_text):
    prompt = f"""
    Extract structured information from the following job description.

    job description:
    {job_description_text}

    Extract:
    - job title
    - job description
    - required skills
    - qualifications
    - responsibilities
    - experience level

    Return only information that is present in the job description.
    Do not invent information.
"""
    result = structured_llm.invoke(prompt)
    return result

