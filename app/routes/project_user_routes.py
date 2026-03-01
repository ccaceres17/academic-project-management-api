from fastapi import APIRouter
from controllers.project_user_controller import ProjectUserController
from models.project_user_model import ProjectUser

router = APIRouter()
controller = ProjectUserController()

@router.post("/project-users")
def assign_user(assignment: ProjectUser):
    return controller.assign_user(assignment)

@router.get("/project-users")
def get_assignments():
    return controller.get_assignments()