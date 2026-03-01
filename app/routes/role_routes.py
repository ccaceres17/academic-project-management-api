from fastapi import APIRouter
from controllers.role_controller import RoleController
from models.role_model import Role

router = APIRouter()
controller = RoleController()

@router.post("/roles")
def create_role(role: Role):
    return controller.create_role(role)

@router.get("/roles")
def get_roles():
    return controller.get_roles()