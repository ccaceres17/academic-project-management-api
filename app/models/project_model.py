from pydantic import BaseModel

class Project(BaseModel):
    id: int = None
    project_name: str
    description: str
    start_date: str
    end_date: str
    id_status: int
    id_research_line: int
    created_by: int