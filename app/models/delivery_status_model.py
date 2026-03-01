from pydantic import BaseModel

class DeliveryStatus(BaseModel):
    id: int = None
    status_name: str
    description: str