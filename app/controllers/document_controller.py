import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.document_model import Document
from fastapi.encoders import jsonable_encoder

class DocumentController:

    def upload(self, document: Document):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO document (id_project, id_user, id_document_type, file_name, file_path, description)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (document.id_project, document.id_user, document.id_document_type,
                  document.file_name, document.file_path, document.description))

            conn.commit()
            return {"result": "Document uploaded"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error uploading document")

        finally:
            if conn:
                conn.close()

    def get_documents(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM document")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder(result)