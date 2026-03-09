import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.comment_model import Comment
from fastapi.encoders import jsonable_encoder


class CommentController:

    def create_comment(self, comment: Comment):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO comment
                (id_progress, id_user, content)
                VALUES (%s,%s,%s)
            """, (
                comment.id_progress,
                comment.id_user,
                comment.content
            ))

            conn.commit()
            return {"result": "Comment created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating comment")

        finally:
            conn.close()

    def get_comments(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM comment")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)

    def get_comment(self, id_comment: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM comment WHERE id_comment=%s",
            (id_comment,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Comment not found")

        return jsonable_encoder(result)

    def update_comment(self, id_comment: int, comment: Comment):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE comment
            SET content=%s
            WHERE id_comment=%s
        """, (
            comment.content,
            id_comment
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Comment not found")

        conn.close()
        return {"result": "Comment updated"}

    def delete_comment(self, id_comment: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM comment WHERE id_comment=%s",
            (id_comment,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Comment not found")

        conn.close()
        return {"result": "Comment deleted"}