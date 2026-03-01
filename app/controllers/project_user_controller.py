import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.project_user_model import ProjectUser
from fastapi.encoders import jsonable_encoder

class ProjectUserController:

    def assign_user(self, assignment: ProjectUser):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO project_user (id_project, id_user, id_project_role)
                VALUES (%s, %s, %s)
            """, (assignment.id_project, assignment.id_user, assignment.id_project_role))

            conn.commit()
            return {"result": "User assigned"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error assigning user")

        finally:
            if conn:
                conn.close()

    def get_assignments(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project_user")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder(result)