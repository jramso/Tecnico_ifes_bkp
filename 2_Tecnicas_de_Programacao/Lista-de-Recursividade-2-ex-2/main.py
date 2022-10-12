palavra=str(input('informe uma palavra ao contrário:'))
print('agora escreva "invert(palavra) e pressione enter"')
def invert(palavra):
  if len(palavra)!=1:
    return invert(palavra[1:])+palavra[0]
  else:
    return palavra  

