from flask import Flask, request, render_template, redirect

app = Flask(__name__)
mensajes = []

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return 'Verificación exitosa', 200
    elif request.method == 'POST':
        data = request.get_json()
        mensajes.append(data)
        print("📩 Mensaje recibido:", data)
        return 'ok', 200
    else:
        return '', 200
