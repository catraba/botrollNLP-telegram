import os
from flask import Flask, request

from Telegram import Telegram
from mensajes import messageHandler

bot = Telegram(os.environ['BOT_KEY'])

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    data = request.json

    try:
        chat_id = data['message']['chat']['id']
        mensaje = data['message']['text']
        message_id = data['message']['message_id']

        bot.sendMessage(chat_id, messageHandler(mensaje), message_id)
        
    except:
        pass

    return ''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8443))
    app.run(host='0.0.0.0', port=port, debug=True)
