import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.program_model import Program
from fastapi.encoders import jsonable_encoder


class ProgramController:

    def create_program(self, program: Program):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO program (program_name, id_faculty)
                VALUES (%s, %s)
                RETURNING id_program, program_name, id_faculty
            """, (
                program.program_name,
                program.id_faculty
            ))

            new_program = cursor.fetchone()
            conn.commit()

            return jsonable_encoder(new_program)

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating program")

        finally:
            conn.close()

    def get_programs(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT p.id_program, p.program_name, p.id_faculty, f.faculty_name
            FROM program p
            JOIN faculty f ON p.id_faculty = f.id_faculty
        """)

        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder(result)

    def get_program(self, id_program: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT p.id_program, p.program_name, p.id_faculty, f.faculty_name
            FROM program p
            JOIN faculty f ON p.id_faculty = f.id_faculty
            WHERE p.id_program = %s
        """, (id_program,))

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Program not found")

        return jsonable_encoder(result)

    def update_program(self, id_program: int, program: Program):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE program
            SET program_name = %s, id_faculty = %s
            WHERE id_program = %s
        """, (
            program.program_name,
            program.id_faculty,
            id_program
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Program not found")

        conn.close()
        return {"result": "Program updated"}

    def delete_program(self, id_program: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM program WHERE id_program=%s",
            (id_program,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Program not found")

        conn.close()
        return {"result": "Program deleted"}