import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.scheduled_delivery_model import ScheduledDelivery


class ScheduledDeliveryController:

    def create_delivery(self, delivery: ScheduledDelivery):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO scheduled_delivery
                (id_project, title, due_date, description, id_delivery_status)
                VALUES (%s,%s,%s,%s,%s)
            """, (
                delivery.id_project,
                delivery.title,
                delivery.due_date,
                delivery.description,
                delivery.id_delivery_status
            ))

            conn.commit()
            return {"result": "Delivery created"}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(500, "Error creating delivery")

        finally:
            conn.close()


    def get_deliveries(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM scheduled_delivery")
        result = cursor.fetchall()

        conn.close()
        return jsonable_encoder(result)


    def get_delivery(self, id_delivery: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM scheduled_delivery WHERE id_delivery=%s",
            (id_delivery,)
        )

        result = cursor.fetchone()
        conn.close()

        if not result:
            raise HTTPException(404, "Delivery not found")

        return jsonable_encoder(result)


    def update_delivery(self, id_delivery: int, delivery: ScheduledDelivery):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE scheduled_delivery
            SET title=%s,
                due_date=%s,
                description=%s,
                id_delivery_status=%s
            WHERE id_delivery=%s
        """, (
            delivery.title,
            delivery.due_date,
            delivery.description,
            delivery.id_delivery_status,
            id_delivery
        ))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Delivery not found")

        conn.close()
        return {"result": "Delivery updated"}


    def delete_delivery(self, id_delivery: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM scheduled_delivery WHERE id_delivery=%s",
            (id_delivery,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(404, "Delivery not found")

        conn.close()
        return {"result": "Delivery deleted"}