# Telegram Alert Webhook

Este bot recibe alertas desde TradingView a través de un webhook y las envía a un grupo de Telegram.

## Instrucciones

1. Coloca tu token del bot y chat ID en `main.py`.
2. Despliega en Render o tu servidor favorito.
3. Usa este endpoint en TradingView: `https://TU_DOMINIO/alerta`
4. Envía alertas con este JSON:

```json
{
  "symbol": "XAUUSD",
  "entry": "2350.20",
  "action": "BUY",
  "setup": "Alta Probabilidad",
  "timeframe": "M15"
}
```
