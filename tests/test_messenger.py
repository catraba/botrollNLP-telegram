import pytest

from messenger import messenger
from unshared import BOTNAME


long_text = """
    Esto es un mensaje que va a ser bastante largo,
    vamos a ir contando un poco nuestra vida a ver
    qué le parece a la máquina, si creeo que esto
    es lo suficientemente extenso para que nos lo
    diga o tenemos que escribir más cosas aleatorias.
"""

start_command = ('Comandos disponibles:\n\n'
                '/btc: Valor del bitcoin actual')



@pytest.mark.parametrize(
    "input, expected",
    [
        ('/start', start_command),
        ('/eth', 'Comando no disponible'),
    ]
)
def test_responses(input, expected):
    assert messenger(input) == expected



@pytest.mark.parametrize(
    "input, expected",
    [
        (long_text, str),
        ('/btc', str),
        (f'{BOTNAME} qué opinas de Harry Potter', str),
    ]
)
def test_type_responses(input, expected):
    assert type(messenger(input)) == expected