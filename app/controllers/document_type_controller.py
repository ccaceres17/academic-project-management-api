import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.document_type_model import DocumentType
from fastapi.encoders import jsonable_encoder

class DocumentTypeController:

    def create_type(self, doc_type: DocumentType):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO document_type (document_type_name, description)
                VALUES (%s, %s)
            """, (doc_type.document_type_name, doc_type.description))

            conn.commit()
            return {"result": "Document type created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating document type")

        finally:
            if conn:
                conn.close()

    def get_types(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM document_type")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder([
            {"id_document_type": r[0], "name": r[1], "description": r[2]}
            for r in result
        ])