from fastapi import APIRouter
from app.controllers.project_status_history_controller import ProjectStatusHistoryController
from app.models.project_status_history_model import ProjectStatusHistory

router = APIRouter(tags=["Project Status History"])
controller = ProjectStatusHistoryController()


@router.post("/project-status-history")
def create_history(history: ProjectStatusHistory):
    return controller.create_history(history)


@router.get("/project-status-history")
def get_history():
    return controller.get_history()


@router.get("/project-status-history/{id_history}")
def get_one_history(id_history: int):
    return controller.get_one_history(id_history)


@router.put("/project-status-history/{id_history}")
def update_history(id_history: int, history: ProjectStatusHistory):
    return controller.update_history(id_history, history)


@router.delete("/project-status-history/{id_history}")
def delete_history(id_history: int):
    return controller.delete_history(id_history)