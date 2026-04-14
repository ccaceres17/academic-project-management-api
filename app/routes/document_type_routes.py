from fastapi import APIRouter
from app.controllers.document_type_controller import DocumentTypeController
from app.models.document_type_model import DocumentType

router = APIRouter(tags=["Document Types"])
controller = DocumentTypeController()


@router.post("/document-types")
def create_type(doc_type: DocumentType):
    return controller.create_type(doc_type)


@router.get("/document-types")
def get_types():
    return controller.get_types()


@router.get("/document-types/{id_document_type}")
def get_type(id_document_type: int):
    return controller.get_type(id_document_type)


@router.put("/document-types/{id_document_type}")
def update_type(id_document_type: int, doc_type: DocumentType):
    return controller.update_type(id_document_type, doc_type)


@router.delete("/document-types/{id_document_type}")
def delete_type(id_document_type: int):
    return controller.delete_type(id_document_type)