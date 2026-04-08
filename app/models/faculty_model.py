from pydantic import BaseModel

class Faculty(BaseModel):
    id_faculty: int = None
    faculty_name: str