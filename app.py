from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)
mensajes = []

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Verificación exitosa", 200
    elif request.method == "POST":
        data = request.get_json()
        mensajes.append(data)
        print("📩 Mensaje recibido:", data)
        return "ok", 200

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        telefono = request.form["numero"]
        texto = request.form["mensaje"]
        payload = {
            "recipient_type": "individual",
            "to": telefono,
            "type": "text",
            "text": {"body": texto}
        }
        headers = {
            "D360-API-KEY": "PON_AQUI_TU_API_KEY"
        }
        requests.post("https://waba-v2.360dialog.io/messages", json=payload, headers=headers)
        return redirect("/chat")
    return render_template("chat.html", mensajes=mensajes)
