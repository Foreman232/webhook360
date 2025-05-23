from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    challenge = request.args.get("hub.challenge")
    token = request.args.get("hub.verify_token")

    if mode == "subscribe" and token == "webhook123":
        return challenge, 200
    else:
        return "Error de verificación", 403

@app.route("/", methods=["POST"])
def receive():
    data = request.get_json()
    print("Mensaje recibido:", data)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
