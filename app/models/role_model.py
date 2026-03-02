from pydantic import BaseModel
from typing import Optional

class Role(BaseModel):
    role_name: str
    description: Optional[str] = None