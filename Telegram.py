from dataclasses import dataclass

from requests import post



@dataclass(slots=True)
class Telegram():
    
    __token: str

    @property
    def url(self) -> str:
        return f'https://api.telegram.org/bot{self.__token}/'

    # def getUpdates(self, offset=None) -> dict:
    #     url = get(f'{self.base}getUpdates', 
    #                 data={'offset': offset})

    #     return url.json()

    def send_message(self, chat_id: str, text: str, 
                    reply_to_message_id=None) -> None:
                    
        post(f'{self.url}sendMessage', 
                data={
                    'chat_id': chat_id, 
                    'text': text, 
                    'reply_to_message_id': reply_to_message_id
                })