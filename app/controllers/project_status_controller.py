import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.project_status_model import ProjectStatus
from fastapi.encoders import jsonable_encoder


class ProjectStatusController:

    def create_status(self, status: ProjectStatus):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO project_status (status_name, description)
            VALUES (%s,%s)
        """, (status.status_name, status.description))

        conn.commit()
        conn.close()

        return {"result": "Status created"}

    def get_statuses(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM project_status")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder(result)

    def get_status(self, id_status: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM project_status WHERE id_status=%s",
            (id_status,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Status not found")

        return jsonable_encoder(result)

    def update_status(self, id_status: int, status: ProjectStatus):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE project_status
            SET status_name=%s, description=%s
            WHERE id_status=%s
        """, (status.status_name, status.description, id_status))

        conn.commit()
        conn.close()

        return {"result": "Status updated"}

    def delete_status(self, id_status: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM project_status WHERE id_status=%s",
            (id_status,)
        )

        conn.commit()
        conn.close()

        return {"result": "Status deleted"}