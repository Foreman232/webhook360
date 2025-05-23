
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
socketio = SocketIO(app)
mensajes = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", mensajes=mensajes)

@app.route("/", methods=["POST"])
def send_message():
    numero = request.form["numero"]
    mensaje = request.form["mensaje"]
    payload = {
        "recipient_type": "individual",
        "to": numero,
        "type": "text",
        "text": {"body": mensaje}
    }
    headers = {
        "D360-API-KEY": "yxKGn4IO24k4MRONILaJxG7xAK"
    }
    requests.post("https://waba-v2.360dialog.io/messages", json=payload, headers=headers)
    return redirect("/")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Verificación exitosa", 200
    elif request.method == "POST":
        data = request.get_json()
        mensajes.append(data)
        socketio.emit("nuevo_mensaje", data)
        return "ok", 200

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
