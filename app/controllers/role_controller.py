import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.role_model import Role
from fastapi.encoders import jsonable_encoder

class RoleController:

    def create_role(self, role: Role):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO role (role_name, description)
                VALUES (%s, %s)
            """, (role.role_name, role.description))

            conn.commit()
            return {"result": "Role created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating role")

        finally:
            if conn:
                conn.close()

    def get_roles(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM role")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder([
            {"id_role": r[0], "role_name": r[1], "description": r[2]}
            for r in result
        ])