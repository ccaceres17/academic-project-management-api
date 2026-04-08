import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.faculty_model import Faculty
from fastapi.encoders import jsonable_encoder


class FacultyController:

    def create_faculty(self, faculty: Faculty):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO faculty (faculty_name)
                VALUES (%s)
                RETURNING id_faculty, faculty_name
            """, (faculty.faculty_name,))

            new_faculty = cursor.fetchone()
            conn.commit()

            return jsonable_encoder(new_faculty)

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating faculty")

        finally:
            conn.close()

    def get_faculties(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM faculty")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)

    def get_faculty(self, id_faculty: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM faculty WHERE id_faculty=%s",
            (id_faculty,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Faculty not found")

        return jsonable_encoder(result)

    def update_faculty(self, id_faculty: int, faculty: Faculty):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE faculty
            SET faculty_name=%s
            WHERE id_faculty=%s
        """, (
            faculty.faculty_name,
            id_faculty
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Faculty not found")

        conn.close()
        return {"result": "Faculty updated"}

    def delete_faculty(self, id_faculty: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM faculty WHERE id_faculty=%s",
            (id_faculty,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Faculty not found")

        conn.close()
        return {"result": "Faculty deleted"} 