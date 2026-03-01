from pydantic import BaseModel

class ResearchLine(BaseModel):
    id: int = None
    research_line_name: str
    description: str