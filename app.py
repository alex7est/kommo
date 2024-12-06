from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os
from Gsheets import findValue

load_dotenv("tk.env")

app = Flask(__name__)

T_ESTADO = 1281987 
KOMMO_DOMAIN = "teccomcuenca" 
ACCESS_TOKEN = os.getenv("KOMMO_ACCES_TOKEN")

@app.route("/webhook", methods=["POST"])
def update_lead():
    # Los datos llegan en formato x-www-form-urlencoded
    data = request.form.to_dict()  # Convierte los datos a un diccionario
    lead_id = data["leads[add][0][id]"] 
    value = findValue(lead_id)

    if not value:
        return jsonify({"error": "Valor no encontrado"}), 400

    # Llamar a la API de Kommo para actualizar el lead
    url = f"https://{KOMMO_DOMAIN}.kommo.com/api/v4/leads/{lead_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "id": int(lead_id),
        "custom_fields_values": [
            {
                "field_id": T_ESTADO,
                "values": [
                    {
                        "value": value
                    }
                ]
            }
        ]
    }

    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        return jsonify({"message": "Lead updated successfully"}), 200
    else:
        return jsonify({"error": response.json()}), response.status_code

@app.route("/", methods=["HEAD"])
def update_lead():
    return jsonify({"message": "Server kept alive"}), 200

if __name__ == "__main__":
    app.run(port=5000)
