from fastapi import FastAPI, UploadFile, File, Form
import tempfile
import os



from .resume_parser import extract_text_from_pdf
from .skill_matcher import match_skills

app = FastAPI() 


@app.post("/")
def home():
    return {
        "message": "Welcome to the Resume Analyzer API. Use the /analyze endpoint to analyze resumes."
    }

@app.post("/analyze")
async def analyze(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)

):

    if resume_file.content_type != "application/pdf":
                return {"error": "Invalid file type. Please upload a PDF file."}
    if not job_description:
                return {"error": "Job description is required."}
    if not resume_file.filename.endswith(".pdf"):
                return {"error": "Invalid file extension. Please upload a PDF file."}
    if job_description.strip() == "":
                return {"error": "Job description cannot be empty. Please provide a valid job description."}
    
    #save the uploaded resume file to a tempory file
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
        
    )as temp_file:
        temp_file.write(await resume_file.read())
        resume_file_path = temp_file.name

    try:

        # Extract resume text
        resume_text = extract_text_from_pdf(resume_file_path)

        # Skill matching
        matching_result = match_skills(
            resume_text,
            job_description
        )


        return {
            "matching": matching_result
        }

    finally:

        # Delete temporary PDF
        os.remove(resume_file_path)

    




