import requests
from bs4 import BeautifulSoup

class MonedasV():
    def __init__(self, moneda):
        self.url = 'https://es.investing.com/crypto/{}'.format(moneda)

    def extrarPrecio(self):
        headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}

        html = requests.get(self.url, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('span'):
            if link.get('id') == 'last_last':
                valor = link.string

        return '$' + valor

class Vacunas():
    def estadoVacunas():
        headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}

        html = requests.get('https://covid-vacuna.app/', headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')

        valor = float(soup.progress['value'])

        fechas = []

        for link in soup.find_all('time'):
            fechas.append(link.text)

        estado = 'Población vacunada: ' + str(round(valor, 2)) + '%\n\nEstimación 75% vacunados: ' + fechas[-2]
    
        return estado
