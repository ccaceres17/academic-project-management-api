import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.project_user_model import ProjectUser


class ProjectUserController:

    def assign_user(self, assignment: ProjectUser):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO project_user
                (id_project, id_user, id_role, assigned_date)
                VALUES (%s,%s,%s,%s)
            """, (
                assignment.id_project,
                assignment.id_user,
                assignment.id_role,
                assignment.assigned_date
            ))

            conn.commit()
            return {"result": "User assigned to project"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error assigning user")

        finally:
            conn.close()


    def get_assignments(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM project_user")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_assignment(self, id_project_user: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM project_user WHERE id_project_user=%s",
            (id_project_user,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Assignment not found")

        return jsonable_encoder(result)


    def update_assignment(self, id_project_user: int, assignment: ProjectUser):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE project_user
            SET id_role=%s
            WHERE id_project_user=%s
        """, (
            assignment.id_role,
            id_project_user
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Assignment not found")

        conn.close()
        return {"result": "Assignment updated"}


    def delete_assignment(self, id_project_user: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM project_user WHERE id_project_user=%s",
            (id_project_user,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Assignment not found")

        conn.close()
        return {"result": "Assignment deleted"}