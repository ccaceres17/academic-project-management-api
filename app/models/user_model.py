from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    password_hash: str
    phone: Optional[str] = None
    id_role: int
    is_active: bool = True