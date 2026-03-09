import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.document_model import Document


class DocumentController:

    def create_document(self, document: Document):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO document
                (id_project, id_user, id_document_type, file_name, file_path, description)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (
                document.id_project,
                document.id_user,
                document.id_document_type,
                document.file_name,
                document.file_path,
                document.description
            ))

            conn.commit()
            return {"result": "Document created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating document")

        finally:
            conn.close()


    def get_documents(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM document")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_document(self, id_document: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM document WHERE id_document=%s",
            (id_document,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Document not found")

        return jsonable_encoder(result)


    def update_document(self, id_document: int, document: Document):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE document
            SET file_name=%s,
                file_path=%s,
                description=%s
            WHERE id_document=%s
        """, (
            document.file_name,
            document.file_path,
            document.description,
            id_document
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Document not found")

        conn.close()
        return {"result": "Document updated"}


    def delete_document(self, id_document: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM document WHERE id_document=%s",
            (id_document,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Document not found")

        conn.close()
        return {"result": "Document deleted"}