from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_message = request.form["message"]
        messages.append({"from": "you", "text": user_message})
        return redirect("/")
    return render_template("index.html", messages=messages)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    text = data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}).get("messages", [{}])[0].get("text", {}).get("body", "")
    if text:
        messages.append({"from": "wa", "text": text})
    return "ok", 200

if __name__ == "__main__":
    app.run()