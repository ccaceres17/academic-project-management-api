from pydantic import BaseModel

class DocumentType(BaseModel):
    id: int = None
    document_type_name: str
    description: str