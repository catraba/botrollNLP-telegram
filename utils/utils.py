from json import load
from os import getcwd

from requests import get as rget

from ..unshared import URL_S3



def json_replies() -> dict:
    f = open(f'{getcwd()}/utils/replies.json', 
            encoding='utf-8',
            mode='r'
        )

    replies = load(f)

    f.close()

    return replies


def write_response_to_csv(msg: str, res: str) -> None:
    rget(URL_S3, params={"msg": msg, "res": res})