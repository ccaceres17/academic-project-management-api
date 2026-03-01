from pydantic import BaseModel

class Role(BaseModel):
    id: int = None
    role_name: str
    description: str