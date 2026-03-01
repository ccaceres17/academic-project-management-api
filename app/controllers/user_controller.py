import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.user_model import User
from fastapi.encoders import jsonable_encoder

class UserController:

    def create_user(self, user: User):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO user_account (first_name, last_name, email, password_hash, phone, id_role)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (user.first_name, user.last_name, user.email, user.password_hash, user.phone, user.id_role))

            conn.commit()
            return {"resultado": "Usuario creado"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear usuario")

        finally:
            if conn:
                conn.close()

    def get_user(self, id_user: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM user_account WHERE id_user = %s", (id_user,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return jsonable_encoder({
                "id_user": result[0],
                "first_name": result[1],
                "last_name": result[2],
                "email": result[3],
                "phone": result[5],
                "id_role": result[6],
                "is_active": result[7],
                "created_at": result[8]
            })

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error al obtener usuario")

        finally:
            if conn:
                conn.close()

    def get_users(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM user_account")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay usuarios")

            payload = [
                {
                    "id_user": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "phone": row[5],
                    "id_role": row[6],
                    "is_active": row[7],
                    "created_at": row[8]
                }
                for row in result
            ]

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error al obtener usuarios")

        finally:
            if conn:
                conn.close()

    def update_user(self, id_user: int, user: User):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE user_account
                SET first_name = %s,
                    last_name = %s,
                    email = %s,
                    phone = %s
                WHERE id_user = %s
            """, (user.first_name, user.last_name, user.email, user.phone, id_user))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return {"resultado": "Usuario actualizado"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar usuario")

        finally:
            if conn:
                conn.close()

    def delete_user(self, id_user: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM user_account WHERE id_user = %s", (id_user,))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return {"resultado": "Usuario eliminado"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar usuario")

        finally:
            if conn:
                conn.close()