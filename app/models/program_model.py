from pydantic import BaseModel

class Program(BaseModel):
    id_program: int = None
    program_name: str
    id_faculty: int