from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        data = request.get_json()
        print("📩 Mensaje recibido del webhook:", data)
        return "ok", 200

if __name__ == "__main__":
    app.run()
