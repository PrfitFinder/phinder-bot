from flask import Flask, request
import requests

app = Flask(__name__)

# Token del bot de Telegram
BOT_TOKEN = '7664866864:AAHr_QWJqM5mwPOEx449s3IAd2Kx5hRuTA4'

# ID de chat (en este caso, tu cuenta personal)
CHAT_ID = '1384640313'

@app.route('/')
def home():
    return '✅ Webhook activo', 200

@app.route('/alerta', methods=['POST'])
def alerta():
    data = request.get_json()
    print("📩 Datos recibidos:", data)

    if not data:
        return '❌ No se recibió JSON', 400

mensaje = f"""
📡 *Señal de TradingView*
🔍 Estrategia: *{data.get('strategy', '❓')}*
🧠 Setup: `{data.get('setup', '❓')}`
📊 Símbolo: `{data.get('symbol', '❓')}`

📥 Entrada: `{data.get('entry', '❓')}`
🛑 Stop Loss: `{data.get('stoploss', '❓')}`

🎯 Take Profit:
- TP1: `{data.get('tp1', '❓')}`
- TP2: `{data.get('tp2', '❓')}`
- TP3: `{data.get('tp3', '❓')}`

🕒 Temporalidad: `{data.get('timeframe', '❓')}`
"""

    # Enviar a Telegram
    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mensaje,
            "parse_mode": "Markdown"
        }
    )

    if response.status_code != 200:
        print("❌ Error enviando a Telegram:", response.text)
        return '❌ Error al enviar a Telegram', 500

    return '✅ Mensaje enviado', 200

if __name__ == '__main__':
    app.run(debug=True)
