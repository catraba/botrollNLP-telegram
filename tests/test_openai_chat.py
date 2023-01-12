import pytest

from openai_chat import gen_chat_response


def test_response():
    mes = 'Hola amigo, ¿cómo estás?'

    assert type(gen_chat_response(mes)) == str