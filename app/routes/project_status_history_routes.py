from fastapi import APIRouter
from controllers.project_status_history_controller import ProjectStatusHistoryController
from models.project_status_history_model import ProjectStatusHistory

router = APIRouter()
controller = ProjectStatusHistoryController()

@router.post("/project-status-history")
def add_history(history: ProjectStatusHistory):
    return controller.add_history(history)