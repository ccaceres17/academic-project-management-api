from fastapi import APIRouter
from controllers.project_role_controller import ProjectRoleController
from models.project_role_model import ProjectRole

router = APIRouter()
controller = ProjectRoleController()

@router.post("/project-roles")
def create_role(role: ProjectRole):
    return controller.create_role(role)

@router.get("/project-roles")
def get_roles():
    return controller.get_roles()