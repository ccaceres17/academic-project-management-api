from fastapi import APIRouter
from app.controllers.program_controller import ProgramController
from app.models.program_model import Program

router = APIRouter(tags=["Program"])
controller = ProgramController()


@router.post("/program")
def create_program(program: Program):
    return controller.create_program(program)


@router.get("/program")
def get_programs():
    return controller.get_programs()


@router.get("/program/{id_program}")
def get_program(id_program: int):
    return controller.get_program(id_program)


@router.put("/program/{id_program}")
def update_program(id_program: int, program: Program):
    return controller.update_program(id_program, program)


@router.delete("/program/{id_program}")
def delete_program(id_program: int):
    return controller.delete_program(id_program)