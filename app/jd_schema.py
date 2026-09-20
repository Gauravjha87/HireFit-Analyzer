from pydantic import BaseModel, Field
from typing import List, Optional

class JobDescriptionSchema(BaseModel):
    job_title: str = Field(..., description='The title of the job position.')
    job_description: str = Field(..., description='A detailed description of the job responsibilities and requirements.')
    required_skills: List[str] = Field(..., description='A list of skills required for the job position.')
    qualifications: Optional[List[str]] = Field(None, description='A list of qualifications or certifications required for the job position.')  
    responsiblities: Optional[List[str]] = Field(None, description='A list of key responsibilities associated with the job position.')
    experince_level: Optional[str] = Field(None, description='The level of experience required for the job position (e.g., entry-level, mid-level, senior).')

    