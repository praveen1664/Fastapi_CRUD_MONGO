from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
    fullName: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=2022)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullName": "Rohit Pachouli",
                "email": "rohit_pachouli@optum.com",
                "course_of_study": "Computer Application (Python)",
                "year": 2011,
                "gpa": "3.9",
            }
        }

class UpdateStudentSchema(BaseModel):
    fullName: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
