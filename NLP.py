from spacy import load
from spacy.matcher import Matcher

from re import match

nlp = load('es_core_news_sm', disable=["tok2vec", "lemmatizer", "ner"])

    
def handling(mensaje):
    #faltas_ortograficas = ["aki", "alante", "ami", "asin", "aver", "llendo", "haiga", "hoygan", "na", "pa", "pal"]
    
    # Detección de URL
    url_patron = r'.*\:\/\/(?:www.)?([^\/]+)'

    # Detección de risas
    jaj_patron = r'((J|j|A|a)[ja]+){2,}'


    Madrid_gen = {
                'FemSing': 'La mejor',
                'FemPlur': 'Las mejores',
                'MascSing': 'El mejor',
                'MascPlur': 'Los mejores'
                }


    doc = nlp(mensaje)

    # Matcher para reconocer patrones
    ciudad = [{"ENT_TYPE": "LOC", "DEP": {"NOT_IN": ["advmod"]}, "LENGTH": {">=": 3}}]

    matcher = Matcher(nlp.vocab)
    matcher.add("Mejor en MADRID", [ciudad])


    for _, start, end in matcher(doc):
        span = doc[start:end]

        if span is not None:
            for token in doc:
                if token.dep_ == 'ROOT':
                    jaj_match = match(jaj_patron, mensaje)

                    if not jaj_match:
                        try:
                            genero = token.morph.get('Gender')
                            numero = token.morph.get('Number')

                            return(Madrid_gen.get(genero[0] + numero[0]) + ' ' + token.text + ' en Madrid')

                        except:
                            pass


    for token in doc:
    # Detección de URLs
        if not token.ent_type_:
            url_match = match(url_patron, mensaje)

            if url_match:
                return('Ni con tu Wi-Fi')