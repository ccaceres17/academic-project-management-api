from pydantic import BaseModel

class Progress(BaseModel):
    id: int = None
    id_project: int
    id_user: int
    description: str
    progress_percentage: float