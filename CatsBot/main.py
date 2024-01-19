import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN = os.getenv('TOKEN')
ERROR_TEXT = 'Здесь должна быть картинка котика :('
offset = -2
timeout = 60
updates: dict
cat_response: requests.Response
cat_link: str

def do_something() -> None:
    print('There was an update')

while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1 }&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&text={ERROR_TEXT}')

    end_time = time.time()
    print(f'Response delay time: {end_time - start_time}')