from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

# Coloca a tua chave da OpenWeather (regista grátis em openweathermap.org)
WEATHER_API_KEY = "TUA_CHAVE_API_AQUI"

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    # Pega a mensagem que o user mandou
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.values.get('From', '')
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "oi" or incoming_msg == "olá":
        msg.body("Olá! Manda o nome de uma cidade para ver o tempo. Ex: luanda")
        return str(resp)

    # Busca o tempo
    cidade = incoming_msg.capitalize()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={WEATHER_API_KEY}&units=metric&lang=pt"
    
    try:
        response = requests.get(url).json()
        if response.get('cod') == 200:
            tempo = response['weather'][0]['description']
            temp = response['main']['temp']
            hum = response['main']['humidity']
            reply = f"Em {cidade}:\n🌤️ {tempo.capitalize()}\n🌡️ {temp}°C\n💧 Humidade: {hum}%"
            msg.body(reply)
        else:
            msg.body("Cidade não encontrada 😕 Tenta outra, ex: luanda, lisboa")
    except:
        msg.body("Erro ao buscar o tempo... tenta mais tarde!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)