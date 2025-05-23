from flask import Flask, request, render_template, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("WhatsAppInbox").sheet1

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Verificación exitosa", 200
    elif request.method == "POST":
        data = request.get_json()
        try:
            msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
            wa_id = msg.get("from", "")
            text = msg.get("text", {}).get("body", "")
            sheet.append_row([wa_id, text])
        except Exception as e:
            print("Error:", e)
        return "ok", 200
    return "", 200

@app.route("/chat", methods=["GET"])
def chat():
    return render_template("chat.html")

@app.route("/inbox", methods=["GET"])
def inbox():
    rows = sheet.get_all_records()
    return render_template("inbox.html", mensajes=rows)
