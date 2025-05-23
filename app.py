from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)
mensajes = []

@app.route("/")
def home():
    return render_template("inbox.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

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
    headers = {
        "Authorization": "Bearer yxKGn4IO24k4MRONILaJxG7xAK",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": data["numero"],
        "type": "text",
        "text": {
            "body": data["mensaje"]
        }
    }
    response = requests.post("https://waba-v2.360dialog.io/messages", headers=headers, json=payload)
    return response.json()
