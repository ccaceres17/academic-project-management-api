from pydantic import BaseModel

class ProjectStatus(BaseModel):
    id: int = None
    status_name: str
    description: str