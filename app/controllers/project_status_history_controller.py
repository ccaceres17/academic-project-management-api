import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.project_status_history_model import ProjectStatusHistory
from fastapi.encoders import jsonable_encoder

class ProjectStatusHistoryController:

    def add_history(self, history: ProjectStatusHistory):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO project_status_history
                (id_project, id_previous_status, id_new_status, changed_by)
                VALUES (%s, %s, %s, %s)
            """, (history.id_project, history.id_previous_status,
                  history.id_new_status, history.changed_by))

            conn.commit()
            return {"result": "History added"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error adding history")

        finally:
            if conn:
                conn.close()