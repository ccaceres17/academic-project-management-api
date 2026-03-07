from pydantic import BaseModel
from datetime import date
from typing import Optional

class Project(BaseModel):
    id_project: Optional[int] = None
    project_name: str
    description: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    id_status: int
    id_research_group: Optional[int] = None
    created_by: int