import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.research_line_model import ResearchLine


class ResearchLineController:

    def create_line(self, line: ResearchLine):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO research_line (research_line_name, description)
                VALUES (%s,%s)
            """, (line.research_line_name, line.description))

            conn.commit()
            return {"result": "Research line created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating research line")

        finally:
            conn.close()


    def get_lines(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM research_line")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_line(self, id_research_line: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM research_line WHERE id_research_line=%s",
            (id_research_line,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Research line not found")

        return jsonable_encoder(result)


    def update_line(self, id_research_line: int, line: ResearchLine):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE research_line
            SET research_line_name=%s,
                description=%s
            WHERE id_research_line=%s
        """, (line.research_line_name, line.description, id_research_line))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Research line not found")

        conn.close()
        return {"result": "Research line updated"}


    def delete_line(self, id_research_line: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM research_line WHERE id_research_line=%s",
            (id_research_line,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Research line not found")

        conn.close()
        return {"result": "Research line deleted"}