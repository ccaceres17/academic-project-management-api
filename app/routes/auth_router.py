from fastapi import APIRouter
from app.controllers.auth_controller import AuthController

router = APIRouter(tags=["Auth"])
controller = AuthController()


@router.post("/auth/login")
def login(email: str, password: str):
    return controller.login(email, password)