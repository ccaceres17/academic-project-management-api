from fastapi import APIRouter
from controllers.progress_controller import ProgressController
from models.progress_model import Progress

router = APIRouter()
controller = ProgressController()

@router.post("/progress")
def create_progress(progress: Progress):
    return controller.create_progress(progress)