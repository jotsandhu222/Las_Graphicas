import requests

location = "https://maps.app.goo.gl/aKyVGF9V787wzoTN6"

BOT_TOKEN = '7571524500:AAHSHuqrAmMr34aRvtBA44qfZITN5zlZmLc'
CHAT_ID = '6053365697'
MESSAGE = f'🚀 this person needs imidiate attenntion for medical services.its location is {location}'

def send_telegram_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Send the message
result = send_telegram_message(BOT_TOKEN, CHAT_ID, MESSAGE)
print(result)
