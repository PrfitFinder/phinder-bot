from flask import Flask, request
import requests

app = Flask(__name__)

# Bot de Telegram
BOT_TOKEN = '7664866864:AAHr_QWJqM5mwPOEx449s3IAd2Kx5hRuTA4'
CHAT_ID = '-1002432886395'  # Tu chat ID

@app.route('/')
def home():
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": "📡 Webhook activo"
        }
    )
    return '✅ Webhook activo', 200

@app.route('/alerta', methods=['POST'])
def alerta():
    data = request.get_json()
    print("📩 Datos recibidos:", data)

    if not data:
        return '❌ No se recibió JSON', 400

    mensaje = f"""
📡 *Gold Phinder*
📊 Símbolo: `{data.get('symbol', '❓')}`
🕒 Temporalidad: `{data.get('timeframe', '❓')}`
📈 Acción: *{data.get('action', '❓').upper()}*

📥 Entrada: `{data.get('entry', '❓')}`
🛑 Stop Loss: `{data.get('stoploss', '❓')}`

🎯 Take Profits:
- TP1: `{data.get('tp1', '❓')}`
- TP2: `{data.get('tp2', '❓')}`
- TP3: `{data.get('tp3', '❓')}`
"""


    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mensaje.strip()
            # "parse_mode": "Markdown" ← lo eliminamos para evitar errores
        }
    )

    print("🔄 Telegram Response:", response.text)

    if response.status_code != 200:
        return '❌ Error al enviar a Telegram', 500

    return '✅ Mensaje enviado', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
