import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.role_model import Role


class RoleController:

    def create_role(self, role: Role):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO role (role_name, description)
                VALUES (%s,%s)
            """, (role.role_name, role.description))

            conn.commit()
            return {"result": "Role created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating role")

        finally:
            conn.close()


    def get_roles(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM role")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_role(self, id_role: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM role WHERE id_role=%s",
            (id_role,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Role not found")

        return jsonable_encoder(result)


    def update_role(self, id_role: int, role: Role):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE role
            SET role_name=%s,
                description=%s
            WHERE id_role=%s
        """, (role.role_name, role.description, id_role))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Role not found")

        conn.close()
        return {"result": "Role updated"}


    def delete_role(self, id_role: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM role WHERE id_role=%s",
            (id_role,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Role not found")

        conn.close()
        return {"result": "Role deleted"}