from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    email: str
    password_hash: str
    phone: str
    id_role: int
    is_active: bool