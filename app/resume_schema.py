from pydantic import BaseModel, Field

from typing import List, Optional

class ResumeSchema(BaseModel):
    name: str = Field(..., description='The full name of the candidate.')
    email: str = Field(..., description='The email address of the candidate.'),
    phone: Optional[str] = Field(None, description='The phone number of the candidate.')
    skills: List[str] = Field(..., description='A list of skills possessed by the candidate.')
    certifications: Optional[List[str]] = Field(None, description='A list of certifications obtained by the candidate.')

class ExperienceSchema(BaseModel):
    company_name: str = Field(..., description='The name of the company where the candidate has worked.')
    job_title: str = Field(..., description='The job title held by the candidate at the company.')
    start_date: str = Field(..., description='The start date of the candidate\'s employment at the company.')
    end_date: Optional[str] = Field(None, description='The end date of the candidate\'s employment at the company. If currently employed, this can be None.')

class EducationSchema(BaseModel):
    instituation_name: str = Field(..., description='The name of the educational institution attended by the candidate.')
    degree: str = Field(..., description='The degree obtained by the candidate.')
    field_of_study: str = Field(..., description='The field of study of the candidate.')




