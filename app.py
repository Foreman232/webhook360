
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
mensajes = []

@app.route("/")
def home():
    return render_template("inbox.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "entry" in data:
        for entry in data["entry"]:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                for msg in value.get("messages", []):
                    mensajes.append({
                        "from": msg["from"],
                        "text": msg["text"]["body"]
                    })
    return "OK", 200

@app.route("/messages")
def get_messages():
    return jsonify(mensajes)

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    import requests
    headers = {
        "Authorization": "Bearer yxKGn4IO24k4MRONILaJxG7xAK",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": data["to"],
        "type": "text",
        "text": {"body": data["text"]}
    }
    r = requests.post("https://waba-v2.360dialog.io/messages", json=payload, headers=headers)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True)
