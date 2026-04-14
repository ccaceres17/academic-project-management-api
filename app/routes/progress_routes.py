from fastapi import APIRouter
from app.controllers.progress_controller import ProgressController
from app.models.progress_model import Progress

router = APIRouter(tags=["Progress"])
controller = ProgressController()

@router.post("/progress")
def create_progress(progress: Progress):
    return controller.create_progress(progress)


@router.get("/progress")
def get_progress():
    return controller.get_progress()


@router.get("/progress/{id_progress}")
def get_progress_by_id(id_progress: int):
    return controller.get_progress_by_id(id_progress)


@router.put("/progress/{id_progress}")
def update_progress(id_progress: int, progress: Progress):
    return controller.update_progress(id_progress, progress)


@router.delete("/progress/{id_progress}")
def delete_progress(id_progress: int):
    return controller.delete_progress(id_progress)

@router.delete("/project-users/{id_project_user}")
def delete_assignment(id_project_user: int):
    return controller.delete_assignment(id_project_user)