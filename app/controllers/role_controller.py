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

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error creating role")

        finally:
            if conn:
                conn.close()

    def get_roles(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM role")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No roles found")

            payload = [
                {
                    "id_role": r[0],
                    "role_name": r[1],
                    "description": r[2]
                }
                for r in result
            ]

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error getting roles")

        finally:
            if conn:
                conn.close()

    
    def get_role(self, id_role: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM role WHERE id_role = %s",
                (id_role,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Role not found")

            return jsonable_encoder({
                "id_role": result[0],
                "role_name": result[1],
                "description": result[2]
            })

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error getting role")

        finally:
            if conn:
                conn.close()

    
    def update_role(self, id_role: int, role: Role):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE role
                SET role_name = %s,
                    description = %s
                WHERE id_role = %s
            """, (role.role_name, role.description, id_role))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Role not found")

            return {"result": "Role updated"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error updating role")

        finally:
            if conn:
                conn.close()

    
    def delete_role(self, id_role: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM role WHERE id_role = %s",
                (id_role,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Role not found")

            return {"result": "Role deleted"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error deleting role")

        finally:
            if conn:
                conn.close()