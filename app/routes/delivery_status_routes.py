from fastapi import APIRouter
from app.controllers.delivery_status_controller import DeliveryStatusController
from app.models.delivery_status_model import DeliveryStatus

router = APIRouter(tags=["Delivery Status"])
controller = DeliveryStatusController()


@router.post("/delivery-status")
def create_status(status: DeliveryStatus):
    return controller.create_status(status)


@router.get("/delivery-status")
def get_status():
    return controller.get_status()


@router.get("/delivery-status/{id_delivery_status}")
def get_one_status(id_delivery_status: int):
    return controller.get_one_status(id_delivery_status)


@router.put("/delivery-status/{id_delivery_status}")
def update_status(id_delivery_status: int, status: DeliveryStatus):
    return controller.update_status(id_delivery_status, status)


@router.delete("/delivery-status/{id_delivery_status}")
def delete_status(id_delivery_status: int):
    return controller.delete_status(id_delivery_status)