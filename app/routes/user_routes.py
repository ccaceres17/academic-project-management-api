from app.models.user_model import User
from app.controllers.user_controller import UserController
from fastapi import APIRouter

router = APIRouter(tags=["Users"])

controller = UserController()


@router.post("/users")
def create_user(user: User):
    return controller.create_user(user)


@router.get("/users/{id_user}")
def get_user(id_user: int):
    return controller.get_user(id_user)


@router.get("/users")
def get_users():
    return controller.get_users()


@router.put("/users/{id_user}")
def update_user(id_user: int, user: User):
    return controller.update_user(id_user, user)


@router.delete("/users/{id_user}")
def delete_user(id_user: int):
    return controller.delete_user(id_user)