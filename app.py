import requests

CHATWOOT_URL = 'https://webhook360.onrender.com/'
CHATWOOT_TOKEN = 'yxKGn4IO24k4MRONILaJxG7xAK'

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "verificación exitosa", 200
    elif request.method == "POST":
        data = request.get_json()
        print("📩 Mensaje recibido:", data)

        mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        numero = data["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]

        payload = {
            "identifier": numero,
            "source_id": numero,
            "content": mensaje,
            "message_type": "incoming",
        }

        headers = {
            "Content-Type": "application/json",
            "api_access_token": CHATWOOT_TOKEN,
        }

        requests.post(CHATWOOT_URL, json=payload, headers=headers)

        return "ok", 200

