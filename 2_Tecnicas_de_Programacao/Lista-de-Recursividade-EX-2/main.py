frase='nothyp'
def inverta(frase):
  if len(frase)==1:
    return frase
  else:
    return inverta(frase[1:])+ frase[0]

