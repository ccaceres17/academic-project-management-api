from fastapi import APIRouter
from app.controllers.project_status_controller import ProjectStatusController
from app.models.project_status_model import ProjectStatus

router = APIRouter()
controller = ProjectStatusController()

@router.post("/status")
def create_status(status: ProjectStatus):
    return controller.create_status(status)

@router.get("/status")
def get_statuses():
    return controller.get_statuses()

@router.get("/status/{id_status}")
def get_status(id_status: int):
    return controller.get_status(id_status)

@router.put("/status/{id_status}")
def update_status(id_status: int, status: ProjectStatus):
    return controller.update_status(id_status, status)

@router.delete("/status/{id_status}")
def delete_status(id_status: int):
    return controller.delete_status(id_status)