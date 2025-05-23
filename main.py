from flask import Flask, request

app = Flask(__name__)

# Ruta para validación inicial (GET) y recepción de mensajes (POST)
@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return 'Verificación exitosa', 200
    
    if request.method == 'POST':
        data = request.get_json()
        print("📩 Mensaje recibido del webhook:", data)
        return 'ok', 200

if __name__ == '__main__':
    app.run()

