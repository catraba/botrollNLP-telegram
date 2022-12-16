from dataclasses import dataclass

from bs4 import BeautifulSoup
from requests import get



@dataclass(slots=True)
class MoneyV():
    
    _coin: str

    @property
    def url(self) -> str:
        return f'https://coinmarketcap.com/es/currencies/{self._coin}'

    @property
    def headers(self) -> dict:
        return {'user-agent': 
                ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0)' 
                'Gecko/20100101 Firefox/35.0')}

    def extract_price(self) -> str:
        value = 'No encontrada'

        soup = BeautifulSoup(get(self.url, headers=self.headers).text, 
                            'html.parser')

        class_ = soup.find(class_='priceValue')

        if class_:
            value = class_.text

        return value