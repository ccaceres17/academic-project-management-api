import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.project_status_model import ProjectStatus
from fastapi.encoders import jsonable_encoder

class ProjectStatusController:

    def create_status(self, status: ProjectStatus):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO project_status (status_name, description)
                VALUES (%s, %s)
            """, (status.status_name, status.description))

            conn.commit()
            return {"result": "Status created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating status")

        finally:
            if conn:
                conn.close()

    def get_statuses(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project_status")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder([
            {"id_status": r[0], "status_name": r[1], "description": r[2]}
            for r in result
        ])