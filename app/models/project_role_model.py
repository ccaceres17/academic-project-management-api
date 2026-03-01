from pydantic import BaseModel

class ProjectRole(BaseModel):
    id: int = None
    role_name: str
    description: str