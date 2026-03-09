import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.research_group_model import ResearchGroup
from fastapi.encoders import jsonable_encoder


class ResearchGroupController:

    def create_research_group(self, group: ResearchGroup):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO research_group
                (research_group_name, description, id_research_line, created_by)
                VALUES (%s,%s,%s,%s)
            """, (
                group.research_group_name,
                group.description,
                group.id_research_line,
                group.created_by
            ))

            conn.commit()
            return {"result": "Research group created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating research group")

        finally:
            conn.close()

    def get_research_groups(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM research_group")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)

    def get_research_group(self, id_research_group: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM research_group WHERE id_research_group=%s",
            (id_research_group,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Research group not found")

        return jsonable_encoder(result)

    def update_research_group(self, id_research_group: int, group: ResearchGroup):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE research_group
            SET research_group_name=%s,
                description=%s,
                id_research_line=%s,
                created_by=%s
            WHERE id_research_group=%s
        """, (
            group.research_group_name,
            group.description,
            group.id_research_line,
            group.created_by,
            id_research_group
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Research group not found")

        conn.close()
        return {"result": "Research group updated"}

    def delete_research_group(self, id_research_group: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM research_group WHERE id_research_group=%s",
            (id_research_group,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Research group not found")

        conn.close()
        return {"result": "Research group deleted"}