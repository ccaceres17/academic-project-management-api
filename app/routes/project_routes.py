from fastapi import APIRouter
from app.controllers.project_controller import ProjectController
from app.models.project_model import Project

router = APIRouter()
controller = ProjectController()

@router.post("/projects")
def create_project(project: Project):
    return controller.create_project(project)

@router.get("/projects")
def get_projects():
    return controller.get_projects()

@router.get("/projects/{id_project}")
def get_project(id_project: int):
    return controller.get_project(id_project)

@router.put("/projects/{id_project}")
def update_project(id_project: int, project: Project):
    return controller.update_project(id_project, project)

@router.delete("/projects/{id_project}")
def delete_project(id_project: int):
    return controller.delete_project(id_project)