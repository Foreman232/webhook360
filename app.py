from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
mensajes = []

@app.route("/")
def home():
    return render_template("inbox.html", mensajes=mensajes)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "entry" in data:
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                for msg in value.get("messages", []):
                    mensajes.append({
                        "from": msg["from"],
                        "text": msg["text"]["body"]
                    })
    return "OK", 200

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    numero = data.get("numero")
    mensaje = data.get("mensaje")

    headers = {
        "Authorization": "Bearer yxKGn4IO24k4MRONILaJxG7xAK",  # tu token real de 360dialog
        "Content-Type": "application/json"
    }

    payload = {
        "to": numero,
        "type": "text",
        "text": {
            "body": mensaje
        }
    }

    response = requests.post("https://waba-v2.360dialog.io/messages", headers=headers, json=payload)
    return jsonify({"status": response.status_code})
