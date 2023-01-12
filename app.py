from flask import Flask, request

from messenger import messenger
from Telegram import Telegram
from unshared import TELEGRAM_TOKEN


app = Flask(__name__)
bot = Telegram(TELEGRAM_TOKEN)


@app.route('/', methods=['POST'])
def main() -> None:
    data = request.json

    if data['message']['chat']['type'] in ['group', 'supergroup']:
        message = data['message'].get('text')

        if isinstance(message, str):
            bot.send_message(data['message']['chat']['id'],
                            messenger(message),
                            data['message']['message_id'])

    return ''