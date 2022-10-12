import random
import numpy
import time
campo=[]
campoB=[]
bombas=0 #Váriavel que guarda a quantidade de bombas
bandeira=0 #Guarda total de marcaçoes de onde acredita-se que está a bomba
acertos=0 #Guarda total de acertos
tamanho=0 #Tamanho do jogo
print('facil - 5x5')
print('medio - 8x8')
print('dificil - 10x10')

def main():
  tamanho=0
  fase=str(input('escolha a fase que deseja jogar \n  fácil digite: F \n médio digite: M \n díficil digite: D \n nível: '))
  if fase=='f' or fase=='F':
    tamanho=5
  elif fase=='m' or fase=='M':
    tamanho=8
  elif fase=='d' or fase=='D':
    tamanho=10
  else:
    print('por favor insira uma fase válida')
  for l in range(0,tamanho):
    linha=[]
    for c in range(0,tamanho):
      if tamanho==5:
        ids=[' ','*',' ',' ']
        n=random.choice(ids)
      elif tamanho==8:
        ids=[1,2,3,' ']
        n=random.choice(ids)
      elif tamanho==10:
        ids=[1,2,3,4,' ',' ']
        n=random.choice(ids)
      linha.append(n)
    campo.append(linha)
  carrumado=numpy.matrix(campo)
  print('\n',str(carrumado)[1:-1])
  print('\n \n \n')

  def contaBomba():
    #Essa funcao deve contar as bombas ao redor de sua posicao
    # e colocar um valor numerico ou manter vazio dependendo da quantidades de bombas ao redor em qualquer direcao

  def matrizcorrespondente():
    ids=['X','X']
    if fase=='f' or fase=='F':
      tamanho=5
    elif fase=='m' or fase=='M':
      tamanho=8
    elif fase=='d' or fase=='D':
      tamanho=10
    else:
      print('por favor insira uma fase válida')
    for li in range(0,tamanho):
      linhaB=[]
      for co in range(0,tamanho):
        if tamanho==5:
          m=random.choice(ids)
        elif tamanho==8:
          m=random.choice(ids)
        elif tamanho==10:
          m=random.choice(ids)
        linhaB.append(m)
      campoB.append(linhaB)
    cBarrumado=numpy.matrix(campoB)
    
    print('\n',str(cBarrumado)[1:-1])    
  f=matrizcorrespondente()

f=main()

#for l in range(0,tamanho)


