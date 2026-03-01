from fastapi import APIRouter
from controllers.research_line_controller import ResearchLineController
from models.research_line_model import ResearchLine

router = APIRouter()
controller = ResearchLineController()

@router.post("/research-lines")
def create_line(line: ResearchLine):
    return controller.create_line(line)

@router.get("/research-lines")
def get_lines():
    return controller.get_lines()