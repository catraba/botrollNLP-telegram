from flask import Flask, request

from messenger import messenger
from Telegram import Telegram
from unshared import TELEGRAM_TOKEN
from utils.utils import write_response_to_csv


app = Flask(__name__)
bot = Telegram(TELEGRAM_TOKEN)


@app.route('/', methods=['POST'])
def main() -> None:
    data = request.json

    if data['message']['chat']['type'] in ['group', 'supergroup']:
        message = data['message'].get('text')
        reply_too_message = data['message'].get('reply_too_message')

        if isinstance(message, str):
            bot.send_message(data['message']['chat']['id'],
                            messenger(message),
                            data['message']['message_id'])

        if reply_too_message:
            write_response_to_csv(
                reply_too_message['text'],
                message
            )

    return ''