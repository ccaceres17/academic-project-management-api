import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.document_type_model import DocumentType


class DocumentTypeController:

    def create_type(self, doc_type: DocumentType):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO document_type (document_type_name, description)
                VALUES (%s,%s)
            """, (doc_type.document_type_name, doc_type.description))

            conn.commit()
            return {"result": "Document type created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating document type")

        finally:
            conn.close()


    def get_types(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM document_type")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_type(self, id_document_type: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM document_type WHERE id_document_type=%s",
            (id_document_type,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Document type not found")

        return jsonable_encoder(result)


    def update_type(self, id_document_type: int, doc_type: DocumentType):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE document_type
            SET document_type_name=%s,
                description=%s
            WHERE id_document_type=%s
        """, (doc_type.document_type_name, doc_type.description, id_document_type))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Document type not found")

        conn.close()
        return {"result": "Document type updated"}


    def delete_type(self, id_document_type: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM document_type WHERE id_document_type=%s",
            (id_document_type,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Document type not found")

        conn.close()
        return {"result": "Document type deleted"}