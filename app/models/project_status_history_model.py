from pydantic import BaseModel

class ProjectStatusHistory(BaseModel):
    id: int = None
    id_project: int
    id_previous_status: int
    id_new_status: int
    changed_by: int