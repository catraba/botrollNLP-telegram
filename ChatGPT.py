import openai

from tokens import OPENAI_TOKEN


openai.api_key = OPENAI_TOKEN


def gen_chat_response(msg: str) -> str:
    res = openai.Completion.create(
        engine="text-davinci-003",
        prompt=msg.replace('@botname', ''),
        temperature=0.8,
        max_tokens=256,
        #stop="."
    )

    return res["choices"][0]["text"]