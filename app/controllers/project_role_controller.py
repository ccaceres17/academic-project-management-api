import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.project_role_model import ProjectRole
from fastapi.encoders import jsonable_encoder

class ProjectRoleController:

    def create_role(self, role: ProjectRole):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO project_role (role_name, description)
                VALUES (%s, %s)
            """, (role.role_name, role.description))

            conn.commit()
            return {"result": "Project role created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating project role")

        finally:
            if conn:
                conn.close()

    def get_roles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project_role")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder([
            {"id_project_role": r[0], "name": r[1], "description": r[2]}
            for r in result
        ])