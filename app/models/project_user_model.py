from pydantic import BaseModel

class ProjectUser(BaseModel):
    id: int = None
    id_project: int
    id_user: int
    id_project_role: int