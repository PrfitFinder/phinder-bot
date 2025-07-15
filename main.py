from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = 'TU_TOKEN_DEL_BOT'
CHAT_ID = 'ID_DEL_GRUPO_O_CANAL'

@app.route('/')
def home():
    return '✅ Webhook activo', 200

@app.route('/alerta', methods=['POST'])
def alerta():
    data = request.get_json()
    print("📩 Datos recibidos:", data)

    if not data:
        return '❌ No se recibió JSON', 400

    mensaje = f"""📡 Nueva Alerta
Símbolo: {data.get('symbol', '❓')}
Dirección: {data.get('action', '❓')}
Entrada: {data.get('entry', '❓')}
Setup: {data.get('setup', '❓')}
Temporalidad: {data.get('timeframe', '❓')}
    """

    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={{
        "chat_id": CHAT_ID,
        "text": mensaje
    }})

    return '✅ Mensaje enviado', 200

if __name__ == '__main__':
    app.run(debug=True)
