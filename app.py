from flask import Flask, request, render_template, jsonify
import datetime

app = Flask(__name__)
mensajes = []

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return 'Verificación exitosa', 200
    elif request.method == "POST":
        data = request.get_json()
        print("📩 Mensaje recibido:", data)
        mensajes.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "from": data["entry"][0]["changes"][0]["value"]["messages"][0]["from"],
            "body": data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        })
        return "ok", 200
    return "", 200

@app.route("/chat", methods=["GET"])
def chat():
    return render_template("chat.html")

@app.route("/inbox", methods=["GET"])
def inbox():
    return render_template("inbox.html", mensajes=mensajes)