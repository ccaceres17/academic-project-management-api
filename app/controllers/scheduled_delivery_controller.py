import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.scheduled_delivery_model import ScheduledDelivery
from fastapi.encoders import jsonable_encoder

class ScheduledDeliveryController:

    def create_delivery(self, delivery: ScheduledDelivery):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO scheduled_delivery
                (id_project, title, due_date, description, id_delivery_status)
                VALUES (%s, %s, %s, %s, %s)
            """, (delivery.id_project, delivery.title,
                  delivery.due_date, delivery.description,
                  delivery.id_delivery_status))

            conn.commit()
            return {"result": "Delivery scheduled"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error scheduling delivery")

        finally:
            if conn:
                conn.close()

    def get_deliveries(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM scheduled_delivery")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder(result)