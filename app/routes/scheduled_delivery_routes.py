from fastapi import APIRouter
from app.controllers.scheduled_delivery_controller import ScheduledDeliveryController
from app.models.scheduled_delivery_model import ScheduledDelivery

router = APIRouter(tags=["Scheduled Deliveries"])
controller = ScheduledDeliveryController()


@router.post("/scheduled-deliveries")
def create_delivery(delivery: ScheduledDelivery):
    return controller.create_delivery(delivery)


@router.get("/scheduled-deliveries")
def get_deliveries():
    return controller.get_deliveries()


@router.get("/scheduled-deliveries/{id_delivery}")
def get_delivery(id_delivery: int):
    return controller.get_delivery(id_delivery)


@router.put("/scheduled-deliveries/{id_delivery}")
def update_delivery(id_delivery: int, delivery: ScheduledDelivery):
    return controller.update_delivery(id_delivery, delivery)


@router.delete("/scheduled-deliveries/{id_delivery}")
def delete_delivery(id_delivery: int):
    return controller.delete_delivery(id_delivery)