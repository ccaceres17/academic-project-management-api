import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.delivery_status_model import DeliveryStatus


class DeliveryStatusController:

    def create_status(self, status: DeliveryStatus):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO delivery_status (status_name, description)
                VALUES (%s,%s)
            """, (status.status_name, status.description))

            conn.commit()
            return {"result": "Delivery status created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating delivery status")

        finally:
            conn.close()


    def get_statuses(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM delivery_status")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_status(self, id_delivery_status: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM delivery_status WHERE id_delivery_status=%s",
            (id_delivery_status,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Delivery status not found")

        return jsonable_encoder(result)


    def update_status(self, id_delivery_status: int, status: DeliveryStatus):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE delivery_status
            SET status_name=%s,
                description=%s
            WHERE id_delivery_status=%s
        """, (status.status_name, status.description, id_delivery_status))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Delivery status not found")

        conn.close()
        return {"result": "Delivery status updated"}


    def delete_status(self, id_delivery_status: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM delivery_status WHERE id_delivery_status=%s",
            (id_delivery_status,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Delivery status not found")

        conn.close()
        return {"result": "Delivery status deleted"}