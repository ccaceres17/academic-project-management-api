from pydantic import BaseModel

class ProjectStatus(BaseModel):
    id_status: int | None = None
    status_name: str
    description: str | None = None