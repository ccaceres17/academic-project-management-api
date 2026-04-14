from fastapi import APIRouter, Depends
from app.controllers.project_controller import ProjectController
from app.models.project_model import Project


from app.middleware.auth_middleware import get_current_user
from app.utils.roles import authorize_roles

router = APIRouter(tags=["Projects"])
controller = ProjectController()


@router.post("/projects")
def create_project(project: Project, user=Depends(get_current_user)):
    authorize_roles(user, ["Teacher", "Coordinator"])
    return controller.create_project(project)



@router.get("/projects")
def get_projects(user=Depends(get_current_user)):
    return controller.get_projects()



@router.get("/projects/{id_project}")
def get_project(id_project: int, user=Depends(get_current_user)):
    return controller.get_project(id_project)



@router.put("/projects/{id_project}")
def update_project(id_project: int, project: Project, user=Depends(get_current_user)):
    authorize_roles(user, ["Teacher", "Coordinator"])
    return controller.update_project(id_project, project)


# 
@router.delete("/projects/{id_project}")
def delete_project(id_project: int, user=Depends(get_current_user)):
    authorize_roles(user, ["Coordinator"])
    return controller.delete_project(id_project)



@router.put("/projects/{id_project}/status")
def update_project_status(id_project: int, id_new_status: int, user=Depends(get_current_user)):
    authorize_roles(user, ["Coordinator"])

    return controller.update_project_status(
        id_project,
        id_new_status,
        user["id_user"]
    )