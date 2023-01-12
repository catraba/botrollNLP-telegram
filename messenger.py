from random import choice, randint
from re import match

from openai_chat import gen_chat_response
from LocAndEur import LocAndEur
from MoneyV import MoneyV
from utils.constants import jaj, www
from utils.utils import json_replies
from unshared import BOTNAME


replies = json_replies()


def messenger(message: str) -> str:
    words = message.split(' ')

    if len(words) > 67:
        return choice(replies['tocho'])

    elif len(words) == 1 and message.startswith('/'):
        if message == '/start':
            return ('Comandos disponibles:\n\n'
                    '/btc: Valor del bitcoin actual')

        elif message == '/btc':
            return MoneyV('bitcoin').extract_price()

        return 'Comando no disponible'

    elif match(f'(.)*{BOTNAME}(.)*', message):
        return gen_chat_response(message)

    else:
        if randint(1, 2) == 1:
            if match(jaj, message):
                return choice(replies['risa'])

            elif match(www, message):
                return choice(replies['url'])

            elif randint(1, 2) == 1:
                return LocAndEur(message).matcher_loc()

            else:
                if randint(1, 10) == 1:
                    return gen_chat_response(message)

        else:
            for word in words:
                if word in replies['faltas']:
                    return choice(replies['faltas_respuestas'])