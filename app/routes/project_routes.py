from fastapi import APIRouter
from controllers.project_controller import ProjectController
from models.project_model import Project

router = APIRouter()
controller = ProjectController()

@router.post("/projects")
def create_project(project: Project):
    return controller.create_project(project)

@router.get("/projects")
def get_projects():
    return controller.get_projects()