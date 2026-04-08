from fastapi import APIRouter
from app.controllers.faculty_controller import FacultyController
from app.models.faculty_model import Faculty

router = APIRouter(tags=["Faculty"])
controller = FacultyController()


@router.post("/faculty")
def create_faculty(faculty: Faculty):
    return controller.create_faculty(faculty)


@router.get("/faculty")
def get_faculties():
    return controller.get_faculties()


@router.get("/faculty/{id_faculty}")
def get_faculty_by_id(id_faculty: int):
    return controller.get_faculty(id_faculty)


@router.put("/faculty/{id_faculty}")
def update_faculty(id_faculty: int, faculty: Faculty):
    return controller.update_faculty(id_faculty, faculty)


@router.delete("/faculty/{id_faculty}")
def delete_faculty(id_faculty: int):
    return controller.delete_faculty(id_faculty)