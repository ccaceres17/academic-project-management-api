from pydantic import BaseModel

class ScheduledDelivery(BaseModel):
    id: int = None
    id_project: int
    title: str
    due_date: str
    description: str
    id_delivery_status: int