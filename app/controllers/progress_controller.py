import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.progress_model import Progress
from fastapi.encoders import jsonable_encoder

class ProgressController:

    def create_progress(self, progress: Progress):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO progress (id_project, id_user, description, progress_percentage)
                VALUES (%s, %s, %s, %s)
            """, (progress.id_project, progress.id_user,
                  progress.description, progress.progress_percentage))

            conn.commit()
            return {"result": "Progress created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating progress")

        finally:
            if conn:
                conn.close()