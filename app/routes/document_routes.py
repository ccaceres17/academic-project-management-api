from fastapi import APIRouter
from app.controllers.document_controller import DocumentController
from app.models.document_model import Document

router = APIRouter(tags=["Documents"])
controller = DocumentController()


@router.post("/documents")
def create_document(document: Document):
    return controller.create_document(document)


@router.get("/documents")
def get_documents():
    return controller.get_documents()


@router.get("/documents/{id_document}")
def get_document(id_document: int):
    return controller.get_document(id_document)


@router.put("/documents/{id_document}")
def update_document(id_document: int, document: Document):
    return controller.update_document(id_document, document)


@router.delete("/documents/{id_document}")
def delete_document(id_document: int):
    return controller.delete_document(id_document)