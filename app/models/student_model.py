from pydantic import BaseModel

class Student(BaseModel):
    id_user: int
    semester: int