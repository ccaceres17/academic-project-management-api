from fastapi import APIRouter
from app.controllers.project_user_controller import ProjectUserController
from app.models.project_user_model import ProjectUser

router = APIRouter(tags=["Project Users"])
controller = ProjectUserController()


@router.post("/project-users")
def assign_user(assignment: ProjectUser):
    return controller.assign_user(assignment)


@router.get("/project-users")
def get_assignments():
    return controller.get_assignments()