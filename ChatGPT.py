import openai

from unshared import BOTNAME, OPENAI_TOKEN


openai.api_key = OPENAI_TOKEN


def gen_chat_response(msg: str) -> str:
    res = openai.Completion.create(
        engine="text-davinci-003",
        prompt=msg.replace(BOTNAME, ''),
        max_tokens=256,
        temperature=0.9,
        n=1
    )

    return res["choices"][0]["text"]