
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Mensaje recibido:", data)
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(debug=True)
