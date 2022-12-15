from random import choice, randint
from re import match

from ChatGPT import gen_chat_response
from constants import jaj, www
from json_read import json_replies
from NLP import LocAndEur
from scraping import MoneyV


replies = json_replies()


def messenger(message: str) -> str:
    words = message.split(' ')

    if len(words) > 33:
        return choice(replies['tocho'])

    elif len(words) == 1 and message.startswith('/'):
        if message == '/start':
            return ('Comandos disponibles:\n\n'
                    '/btc: Valor del bitcoin actual')

        elif message == '/btc':
            return MoneyV('bitcoin').extract_price()

        return 'Comando no disponible'

    elif match('(.)*@botname(.)*', message):
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
                if randint(1, 5) == 1:
                    return gen_chat_response(message)

        else:
            for word in words:
                if word in replies['faltas']:
                    return choice(replies['faltas_respuestas'])