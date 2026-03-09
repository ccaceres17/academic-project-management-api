import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.progress_model import Progress
from fastapi.encoders import jsonable_encoder


class ProgressController:

    def create_progress(self, progress: Progress):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO progress
                (id_project, id_user, description, progress_percentage)
                VALUES (%s,%s,%s,%s)
            """, (
                progress.id_project,
                progress.id_user,
                progress.description,
                progress.progress_percentage
            ))

            conn.commit()
            return {"result": "Progress created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating progress")

        finally:
            conn.close()

    def get_progress(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM progress")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)

    def get_progress_by_id(self, id_progress: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM progress WHERE id_progress=%s",
            (id_progress,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Progress not found")

        return jsonable_encoder(result)

    def update_progress(self, id_progress: int, progress: Progress):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE progress
            SET description=%s,
                progress_percentage=%s
            WHERE id_progress=%s
        """, (
            progress.description,
            progress.progress_percentage,
            id_progress
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Progress not found")

        conn.close()
        return {"result": "Progress updated"}

    def delete_progress(self, id_progress: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM progress WHERE id_progress=%s",
            (id_progress,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Progress not found")

        conn.close()
        return {"result": "Progress deleted"}