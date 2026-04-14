from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProjectUser(BaseModel):
    id_project_user: Optional[int] = None
    id_project: int
    id_user: int
    id_role: int
    assigned_date: Optional[date] = None