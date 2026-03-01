import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.comment_model import Comment
from fastapi.encoders import jsonable_encoder

class CommentController:

    def create_comment(self, comment: Comment):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO comment (id_progress, id_user, content)
                VALUES (%s, %s, %s)
            """, (comment.id_progress, comment.id_user, comment.content))

            conn.commit()
            return {"result": "Comment added"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error adding comment")

        finally:
            if conn:
                conn.close()