from spacy import load
from spacy.matcher import Matcher


nlp = load('es_dep_news_trf', disable=["tok2vec", "lemmatizer"])


city = [
    {
        "ENT_TYPE": "LOC", 
        "DEP": {"NOT_IN": ["advmod"]}, 
        "LENGTH": {">=": 4}
    }
]

number = [
    {
        "DEP": "obj", 
        "POS": "NOUN"
    }
]

gen_GN = {
    'FemSing': 'La mejor',
    'FemPlur': 'Las mejores',
    'MascSing': 'El mejor',
    'MascPlur': 'Los mejores'
}

jaj = r'((J|j|A|a)[ja]+){2,}'

www = r'.*\:\/\/(?:www.)?([^\/]+)'


matcher = Matcher(nlp.vocab)
matcher.add("Mejor en MADRID", [city])
matcher.add("Yo siempre le echo 20€", [number])