from pydantic import BaseModel
from datetime import date

class Project(BaseModel):
    id_project: int | None = None
    project_name: str
    description: str | None = None
    start_date: date
    end_date: date | None = None
    id_status: int
    id_research_line: int | None = None
    created_by: int