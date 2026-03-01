from pydantic import BaseModel

class Document(BaseModel):
    id: int = None
    id_project: int
    id_user: int
    id_document_type: int
    file_name: str
    file_path: str
    description: str