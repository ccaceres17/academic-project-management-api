import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.student_model import Student
from fastapi.encoders import jsonable_encoder

class StudentController:

    def create_student(self, student: Student):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO student (id_user, semester)
                VALUES (%s, %s)
            """, (student.id_user, student.semester))

            conn.commit()
            return {"result": "Student created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating student")

        finally:
            if conn:
                conn.close()

    def get_student(self, id_user: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM student WHERE id_user = %s", (id_user,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(status_code=404, detail="Student not found")

        return jsonable_encoder({
            "id_user": result[0],
            "semester": result[1]
        })

    def get_students(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder([
            {"id_user": r[0], "semester": r[1]}
            for r in result
        ])

    def update_student(self, id_user: int, student: Student):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE student
                SET semester = %s
                WHERE id_user = %s
            """, (student.semester, id_user))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student not found")

            return {"result": "Student updated"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error updating student")

        finally:
            if conn:
                conn.close()

    def delete_student(self, id_user: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM student WHERE id_user = %s", (id_user,))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student not found")

            return {"result": "Student deleted"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error deleting student")

        finally:
            if conn:
                conn.close()