from pydantic import BaseModel,EmailStr,Field
from typing import Optional,Annotated


class Student(BaseModel):
    name: str = 'abhit'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Annotated[Optional[float], Field(...,ge=0.0,le = 10.0,description="CGPA must be between 0.0 and 10.0"
                       )]
new_student = {'name':'Alice', 'age': '20', 'email':'abhit@example.com','cgpa':9}

student = Student(**new_student) 

std_dict = dict(student)

print(std_dict)

stud_json = student.model_dump_json()
