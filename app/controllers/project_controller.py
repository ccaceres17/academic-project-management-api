import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.project_model import Project
from fastapi.encoders import jsonable_encoder

class ProjectController:

    def create_project(self, project: Project):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO project (project_name, description, start_date, end_date, id_status, id_research_line, created_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (project.project_name, project.description, project.start_date,
                  project.end_date, project.id_status, project.id_research_line, project.created_by))

            conn.commit()
            return {"result": "Project created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating project")

        finally:
            if conn:
                conn.close()

    def get_projects(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder(result)