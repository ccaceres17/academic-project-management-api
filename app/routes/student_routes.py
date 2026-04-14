from fastapi import APIRouter
from app.controllers.student_controller import StudentController
from app.models.student_model import Student

router = APIRouter()
controller = StudentController()

@router.post("/students")
def create_student(student: Student):
    return controller.create_student(student)

@router.get("/students/{id_user}")
def get_student(id_user: int):
    return controller.get_student(id_user)

@router.get("/students")
def get_students():
    return controller.get_students()

@router.put("/students/{id_user}")
def update_student(id_user: int, student: Student):
    return controller.update_student(id_user, student)

@router.delete("/students/{id_user}")
def delete_student(id_user: int):
    return controller.delete_student(id_user)