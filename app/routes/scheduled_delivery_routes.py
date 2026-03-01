from fastapi import APIRouter
from controllers.scheduled_delivery_controller import ScheduledDeliveryController
from models.scheduled_delivery_model import ScheduledDelivery

router = APIRouter()
controller = ScheduledDeliveryController()

@router.post("/deliveries")
def create_delivery(delivery: ScheduledDelivery):
    return controller.create_delivery(delivery)

@router.get("/deliveries")
def get_deliveries():
    return controller.get_deliveries()