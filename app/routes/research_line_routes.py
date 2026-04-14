from fastapi import APIRouter
from app.controllers.research_line_controller import ResearchLineController
from app.models.research_line_model import ResearchLine

router = APIRouter(tags=["Research Lines"])
controller = ResearchLineController()


@router.post("/research-lines")
def create_line(line: ResearchLine):
    return controller.create_line(line)


@router.get("/research-lines")
def get_lines():
    return controller.get_lines()


@router.get("/research-lines/{id_research_line}")
def get_line(id_research_line: int):
    return controller.get_line(id_research_line)


@router.put("/research-lines/{id_research_line}")
def update_line(id_research_line: int, line: ResearchLine):
    return controller.update_line(id_research_line, line)


@router.delete("/research-lines/{id_research_line}")
def delete_line(id_research_line: int):
    return controller.delete_line(id_research_line)