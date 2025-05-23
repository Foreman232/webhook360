from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "¡Servidor activo correctamente!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Mensaje recibido:", data)
    return "Recibido", 200

