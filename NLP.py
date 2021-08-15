from spacy import load
nlp = load('es_core_news_sm-3.0.0/es_core_news_sm/es_core_news_sm-3.0.0', disable=["lemmatizer", "textcat", "custom"])

from spacy.matcher import Matcher

from re import match

    
def handling(mensaje):
    faltas_ortograficas = ["aki", "alante", "ami", "asin", "aver", "llendo", "haiga", "hoygan", "na", "pa", "pal"]
    false_loc = ['cómo', 'qué', 'movil', 'suena', 'aver']
    url_pattern = r'.*\:\/\/(?:www.)?([^\/]+)'
                           
    doc = nlp(mensaje.lower())
           
    url_match = match(url_pattern, mensaje)
    
    if url_match:
        for token in doc:
            if not token.ent_type_:
                return('Ni con tu Wi-Fi')
        
    for token in doc:
        if token.text in faltas_ortograficas:
            return('Escribe bien o te meto eh')
    
    for palabra in doc.ents:     
        if palabra.label_ == 'LOC':
            if palabra.text not in false_loc:
                
                pattern1 = [{"DEP": {"IN": ["nsubj", "obj"]}},
                            {"OP": "?"}]
                pattern2 = [{"POS": {"IN": ['NOUN']}},
                            {"OP": "?"}]

                matcher = Matcher(nlp.vocab)
                matcher.add("Matcheador", [pattern1, pattern2])

                matches = matcher(doc)
             
                for match_id, start, end in matches:
                    span = doc[start:end]

                    if span is not None:
                        return 'Las mejores ' + span.text + ' en Madrid'
                    else:
                        pass
