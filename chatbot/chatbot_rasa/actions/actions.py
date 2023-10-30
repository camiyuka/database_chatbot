import psycopg2
from rasa_sdk import Action
from rasa_sdk import slot


class ActionConectarDatabase(Action):
    def name(self):
        return "action_database"

    def run(self, dispatcher, tracker, domain):
      
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="pessoas",
            user="postgres",
            password=""
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoas")
        result = cursor.fetchall()

        cursor.close()
        conn.close()
        
        dispatcher.utter_message(f"Resultados da consulta: {result}")

        return []
