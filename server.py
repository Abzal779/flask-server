import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Динамикалық порт орнату
port = int(os.environ.get("PORT", 5000))

ESP8266_IP = "http://192.168.1.100"  # Мұнда ESP IP адресін жаз

@app.route('/')
def home():
    return "Hello, Render!"

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

if __name__ == "__main__":
    # Динамикалық портпен серверді іске қосу
    app.run(host="0.0.0.0", port=port)
import os
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

# Портты орта айнымалысы арқылы алу
port = int(os.environ.get("PORT", 5000))  # Портты environment айнымалысынан алу
app.run(host="0.0.0.0", port=port)  # барлық интерфейстерде тыңдаңыз

