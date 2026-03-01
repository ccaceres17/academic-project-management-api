from fastapi import APIRouter
from controllers.delivery_status_controller import DeliveryStatusController
from models.delivery_status_model import DeliveryStatus

router = APIRouter()
controller = DeliveryStatusController()

@router.post("/delivery-status")
def create_status(status: DeliveryStatus):
    return controller.create_status(status)

@router.get("/delivery-status")
def get_statuses():
    return controller.get_statuses()