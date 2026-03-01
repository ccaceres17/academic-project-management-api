from fastapi import APIRouter
from controllers.project_status_controller import ProjectStatusController
from models.project_status_model import ProjectStatus

router = APIRouter()
controller = ProjectStatusController()

@router.post("/project-status")
def create_status(status: ProjectStatus):
    return controller.create_status(status)

@router.get("/project-status")
def get_statuses():
    return controller.get_statuses()