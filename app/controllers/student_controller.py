import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.student_model import Student


class StudentController:

    def create_student(self, student: Student):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO student (id_user, semester)
                VALUES (%s,%s)
            """, (student.id_user, student.semester))

            conn.commit()
            return {"result": "Student created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating student")

        finally:
            conn.close()


    def get_students(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_student(self, id_user: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM student WHERE id_user=%s",
            (id_user,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Student not found")

        return jsonable_encoder(result)


    def update_student(self, id_user: int, student: Student):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE student
            SET semester=%s
            WHERE id_user=%s
        """, (student.semester, id_user))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Student not found")

        conn.close()
        return {"result": "Student updated"}


    def delete_student(self, id_user: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM student WHERE id_user=%s",
            (id_user,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Student not found")

        conn.close()
        return {"result": "Student deleted"}