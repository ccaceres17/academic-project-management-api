import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.delivery_status_model import DeliveryStatus
from fastapi.encoders import jsonable_encoder

class DeliveryStatusController:

    def create_status(self, status: DeliveryStatus):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO delivery_status (status_name, description)
                VALUES (%s, %s)
            """, (status.status_name, status.description))

            conn.commit()
            return {"result": "Delivery status created"}

        except psycopg2.Error:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail="Error creating delivery status")

        finally:
            if conn:
                conn.close()

    def get_statuses(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM delivery_status")
        result = cursor.fetchall()
        conn.close()

        return jsonable_encoder([
            {"id_delivery_status": r[0], "name": r[1], "description": r[2]}
            for r in result
        ])