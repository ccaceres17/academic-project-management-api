import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.project_status_history_model import ProjectStatusHistory


class ProjectStatusHistoryController:

    def add_history(self, history: ProjectStatusHistory):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO project_status_history
                (id_project, id_previous_status, id_new_status, changed_by)
                VALUES (%s,%s,%s,%s)
            """, (
                history.id_project,
                history.id_previous_status,
                history.id_new_status,
                history.changed_by
            ))

            conn.commit()
            return {"result": "History added"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error adding history")

        finally:
            conn.close()


    def get_history(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM project_status_history")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_project_history(self, id_project: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM project_status_history
            WHERE id_project=%s
        """, (id_project,))

        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder(result)


    def delete_history(self, id_history: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM project_status_history WHERE id_history=%s",
            (id_history,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "History not found")

        conn.close()
        return {"result": "History deleted"}