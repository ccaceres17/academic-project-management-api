from fastapi import APIRouter
from controllers.document_controller import DocumentController
from models.document_model import Document

router = APIRouter()
controller = DocumentController()

@router.post("/documents")
def upload(document: Document):
    return controller.upload(document)

@router.get("/documents")
def get_documents():
    return controller.get_documents()