from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.utils.jwt_handler import create_token


class AuthController:

    def login(self, email: str, password: str):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT u.id_user, u.email, u.password_hash, r.role_name
                FROM user_account u
                JOIN role r ON u.id_role = r.id_role
                WHERE TRIM(LOWER(u.email)) = TRIM(LOWER(%s))
            """, (email,))

            user = cursor.fetchone()

            if not user:
                raise HTTPException(404, "User not found")

        
            if password != user[2]:
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