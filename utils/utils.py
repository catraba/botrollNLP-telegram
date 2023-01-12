from json import load
from os import getcwd


def json_replies() -> dict:
    f = open(f'{getcwd()}/utils/replies.json', 
        encoding='utf-8',
        mode='r')

    replies = load(f)

    f.close()

    return replies