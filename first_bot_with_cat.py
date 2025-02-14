import requests
import time

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN = '7289568184:AAFhXh6UVR0-deFXB6aD-cDkHr4ZGPbp9jo'
TEXT ='Ура!Заработало!'
ERROR_TEXT = 'Здесь должна была быть картинка с котиками:('
MAX_COUNTER = 100

offset = 2
counter = 0
cat_response: requests.Response
chat_id:int
cat_link: str

while counter < MAX_COUNTER:
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1000)
    counter +=1