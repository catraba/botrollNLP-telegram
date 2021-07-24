from spacy import load
nlp = load('es_core_news_sm-3.0.0/es_core_news_sm/es_core_news_sm-3.0.0')

from spacy.matcher import Matcher

'''
from numpy import array, asarray, reshape, argmax
from sklearn.linear_model import LogisticRegression

import os
import json
from random import choice


with open(os.path.join(os.getcwd(), 'conversaciones.json')) as file:
    conversaciones = json.load(file)
    

def lemmatizer(mensaje, frase=''):

    with nlp.disable_pipes():
        for palabra in nlp(mensaje):
            if palabra.is_stop:
                frase = frase + palabra.lemma_ + ' '

        frase = frase[:-1]

    return frase
    

def processing():

    etiquetas = []
    codigos = {}
    docs = []

    for i, intencion in enumerate(conversaciones['intenciones']):
        codigos[i] = intencion['etiqueta']

        with nlp.disable_pipes():
            for patron in intencion['patrones']:
                frase = ''
                for p in nlp(patron):
                    frase = frase + p.lemma_ + ' '

                frase = frase[:-1]
                docs.append(frase)

                etiquetas.append(i)


            vectores = array([nlp(d).vector for d in docs])
            labels = asarray(etiquetas)


    LR = LogisticRegression() #solver="liblinear", max_iter=10000
    modelo = LR.fit(vectores, labels)

    return codigos, modelo


def mencion(mensaje, codigos, modelo):

    patron = nlp(lemmatizer(mensaje)).vector
    patron = patron.reshape(1, -1)

    y_prob = modelo.predict_proba(patron)
    
    maximo = y_prob.max().astype(float)
    indice = argmax(y_prob)

    respuestas = []

    if maximo > 0.8:
        opcion = codigos.get(indice)

        for intencion in conversaciones['intenciones']:
            for respuesta in intencion['respuestas']:
                respuestas.append(respuesta)

        return choice(respuestas)
'''

    
def handling(mensaje
    faltas_ortograficas = ["aki", "alante", "ami", "asin", "aver", "llendo", "haiga", "hoygan", "na", "pa", "pal"]
                           
    doc = nlp(mensaje)
             
    for token in doc:
        if token.text in faltas_ortograficas:
            return('Escribe bien o te meto eh')
    
    for palabra in doc.ents:     
        if palabra.label_ == 'LOC':
            patron = [{"DEP": {"IN": ["nmod", "ROOT"]}, "POS": {"NOT_IN": ["ADP", "PROPN"]}}]

            matcher = Matcher(nlp.vocab)
            matcher.add("Matcheador", [patron])

            matches = matcher(doc)
             
            for match_id, start, end in matches:
                span = doc[start:end]

                if span is not None:
                    return 'Las mejores ' + span.text + ' en Madrid'
                else:
                    pass

            for match_id, start, end in matches:
                span = doc[start:end]

                return 'Best ' + span.text + ' en Madrid'
