import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.research_line_model import ResearchLine
from fastapi.encoders import jsonable_encoder

class ResearchLineController:

    def create_line(self, line: ResearchLine):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO research_line (research_line_name, description)
                VALUES (%s, %s)
            """, (line.research_line_name, line.description))

            conn.commit()
            return {"result": "Research line created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating line")

        finally:
            if conn:
                conn.close()

    def get_lines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM research_line")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder([
            {"id_research_line": r[0], "name": r[1], "description": r[2]}
            for r in result
        ])