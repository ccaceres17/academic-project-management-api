import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.project_model import Project


class ProjectController:

    def create_project(self, project: Project):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO project
                (project_name, description, start_date, end_date,
                 id_status, id_research_group, created_by)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (
                project.project_name,
                project.description,
                project.start_date,
                project.end_date,
                project.id_status,
                project.id_research_group,
                project.created_by
            ))

            conn.commit()
            return {"result": "Project created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating project")

        finally:
            conn.close()


    def get_projects(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM project")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_project(self, id_project: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM project WHERE id_project=%s",
            (id_project,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Project not found")

        return jsonable_encoder(result)


    def update_project(self, id_project: int, project: Project):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE project
            SET project_name=%s,
                description=%s,
                end_date=%s,
                id_status=%s
            WHERE id_project=%s
        """, (
            project.project_name,
            project.description,
            project.end_date,
            project.id_status,
            id_project
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Project not found")

        conn.close()
        return {"result": "Project updated"}


    def delete_project(self, id_project: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM project WHERE id_project=%s",
            (id_project,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Project not found")

        conn.close()
        return {"result": "Project deleted"}