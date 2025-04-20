from flask import Flask, request
import requests

app = Flask(__name__)

ESP8266_IP = "http://192.168.1.100"  # Мұнда ESP IP адресін жаз

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    amount = data.get("amount")

    if not amount:
        return {"error": "Amount missing"}, 400

    try:
        response = requests.get(f"{ESP8266_IP}/start?amount={amount}")
        return {"status": "OK", "esp_response": response.text}
    except Exception as e:
        return {"error": str(e)}, 500

