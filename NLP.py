from random import choice

from constants import gen_GN, matcher, nlp


class LocAndEur():

  def __init__(self, message):
    self.doc = nlp(message)

  def matcher_loc(self) -> str:
    for _, start, end in matcher(self.doc):
      span = self.doc[start:end]

      if span:
        for token in self.doc:
          if token.dep_ == 'obj' and (token.pos_ == 'NOUN' or 'PROPN'):
              try:
                num = int(span.text)

                return choice([('Yo siempre le echo 20 a mi '
                                f'{token.text}'),
                                'Poco me parece'])
                
              except ValueError:
                pass

              gen = token.morph.get('Gender')
              num = token.morph.get('Number')

              millor = gen_GN.get(f'{gen[0]}{num[0]}', 'El mejor')

              return f'{millor} {token.text} en Madrid'