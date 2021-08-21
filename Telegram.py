import requests

class Telegram():
    def __init__(self, token):
        self.base = 'https://api.telegram.org/bot{}/'.format(token)

    def getUpdates(self, offset=None):
        url = requests.get(self.base + 'getUpdates',
                           data={'offset': offset})

        return url.json()

    def sendMessage(self, chat_id, text, reply_to_message_id=None):
        requests.post(self.base + 'sendMessage', 
                      data={'chat_id': chat_id,
                            'text': text,
                            'reply_to_message_id': reply_to_message_id})