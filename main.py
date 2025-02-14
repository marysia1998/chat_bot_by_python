import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7289568184:AAFhXh6UVR0-deFXB6aD-cDkHr4ZGPbp9jo'
TEXT ='Ура!Заработало!'
MAX_COUNTER = 100

offset = 2
counter = 0
chat_id:int

while counter < MAX_COUNTER:
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1000)
    counter +=1