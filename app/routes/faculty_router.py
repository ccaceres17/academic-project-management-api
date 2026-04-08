from fastapi import APIRouter, Depends
from app.controllers.faculty_controller import FacultyController
from app.models.faculty_model import Faculty
from app.middleware.auth_middleware import get_current_user
from app.utils.roles import authorize_roles

router = APIRouter(tags=["Faculty"])
controller = FacultyController()

@router.post("/faculty")
def create_faculty(faculty: Faculty, user=Depends(get_current_user)):
    authorize_roles(user, ["Coordinator"])
    return controller.create_faculty(faculty)


@router.get("/faculty")
def get_faculties(user=Depends(get_current_user)):
    return controller.get_faculties()



@router.get("/faculty/{id_faculty}")
def get_faculty_by_id(id_faculty: int, user=Depends(get_current_user)):
    return controller.get_faculty(id_faculty)


@router.put("/faculty/{id_faculty}")
def update_faculty(id_faculty: int, faculty: Faculty, user=Depends(get_current_user)):
    authorize_roles(user, ["Coordinator"])
    return controller.update_faculty(id_faculty, faculty)


@router.delete("/faculty/{id_faculty}")
def delete_faculty(id_faculty: int, user=Depends(get_current_user)):
    authorize_roles(user, ["Coordinator"])
    return controller.delete_faculty(id_faculty)