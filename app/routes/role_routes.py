from fastapi import APIRouter
from app.controllers.role_controller import RoleController
from app.models.role_model import Role

router = APIRouter()
controller = RoleController()


# CREATE
@router.post("/roles")
def create_role(role: Role):
    return controller.create_role(role)


# GET ALL
@router.get("/roles")
def get_roles():
    return controller.get_roles()


# GET ONE
@router.get("/roles/{id_role}")
def get_role(id_role: int):
    return controller.get_role(id_role)


# UPDATE
@router.put("/roles/{id_role}")
def update_role(id_role: int, role: Role):
    return controller.update_role(id_role, role)


# DELETE
@router.delete("/roles/{id_role}")
def delete_role(id_role: int):
    return controller.delete_role(id_role)