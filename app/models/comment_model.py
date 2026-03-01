from pydantic import BaseModel

class Comment(BaseModel):
    id: int = None
    id_progress: int
    id_user: int
    content: str