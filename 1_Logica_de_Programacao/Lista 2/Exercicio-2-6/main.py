lista=[]

for i in range(0,12):
  lista.append(float(input('Insira o valor: ')))

x=int(input('Insira o valor de X: '))
y=int(input('Insira o valor de y: '))

if (x>=0 and x<=12) and (y>=0 and y<=12):
  if x==12 and y==12:
     x=x-1
     y=y-1
     print('A soma dos elementos da lista \n na posição x e y é: ', (lista[x]+lista[y]))
  elif x==12:
    x=x-1
    print('A soma dos elementos da lista \n na posição x e y é: ', lista[x]+lista[y])
  elif y==12:
    y=y-1
    print('A soma dos elementos da lista \n na posição x e y é: ', lista[x]+lista[y])
  else:
    print('A soma dos elementos da lista \n na posição x e y é: ', lista[x]+lista[y])
 
else:
  print('Valor de x ou y digitado está incorreto')
    