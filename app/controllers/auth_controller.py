from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.utils.jwt_handler import create_token
from app.utils.hash import verify_password


class AuthController:

    def login(self, email: str, password: str):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT u.id_user, u.email, u.password_hash, r.role_name
                FROM user_account u
                JOIN role r ON u.id_role = r.id_role
                WHERE u.email = %s
            """, (email,))

            user = cursor.fetchone()

            if not user:
                raise HTTPException(404, "User not found")

            stored_password = user[2]

            # 🔥 SOPORTE PARA TEXTO PLANO Y HASH
            try:
                password_valid = verify_password(password, stored_password)
            except:
                # fallback si no está hasheado
                password_valid = password == stored_password

            if not password_valid:
                raise HTTPException(401, "Invalid credentials")

            token = create_token({
                "id_user": user[0],
                "role": user[3]
            })

            return {
                "access_token": token,
                "user": {
                    "id_user": user[0],
                    "email": user[1],
                    "role": user[3]
                }
            }

        finally:
            conn.close()