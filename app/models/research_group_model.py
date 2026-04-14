from pydantic import BaseModel
from typing import Optional


class ResearchGroup(BaseModel):
    research_group_name: str
    description: Optional[str] = None
    id_research_line: Optional[int] = None
    created_by: Optional[int] = None