from fastapi import APIRouter
from app.controllers.research_group_controller import ResearchGroupController
from app.models.research_group_model import ResearchGroup

router = APIRouter(tags=["Research Groups"])
controller = ResearchGroupController()


@router.post("/research-groups")
def create_research_group(group: ResearchGroup):
    return controller.create_research_group(group)


@router.get("/research-groups")
def get_research_groups():
    return controller.get_research_groups()


@router.get("/research-groups/{id_research_group}")
def get_research_group(id_research_group: int):
    return controller.get_research_group(id_research_group)


@router.put("/research-groups/{id_research_group}")
def update_research_group(id_research_group: int, group: ResearchGroup):
    return controller.update_research_group(id_research_group, group)


@router.delete("/research-groups/{id_research_group}")
def delete_research_group(id_research_group: int):
    return controller.delete_research_group(id_research_group)