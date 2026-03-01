from fastapi import APIRouter
from controllers.document_type_controller import DocumentTypeController
from models.document_type_model import DocumentType

router = APIRouter()
controller = DocumentTypeController()

@router.post("/document-types")
def create_type(doc_type: DocumentType):
    return controller.create_type(doc_type)

@router.get("/document-types")
def get_types():
    return controller.get_types()