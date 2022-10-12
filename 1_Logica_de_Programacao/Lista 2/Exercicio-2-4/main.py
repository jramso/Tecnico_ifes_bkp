lista=[]

for i in range(0,10):
  lista.append(float (input('Insira o valor na lista: ')))

m=float (input('Insira o valor de M: '))
a= False # variavel pra veririficar se existe a posição M na lista
posi=0 #guardar a posição de i na lista  
for i in range (0,10):
 if m==lista[i]:
  posi=i
  a= True # se for TRUE significa que existe valor M na lista

if a==True:
  print('o valor M se encontra na posição ',posi+1,' da lista')
else:
  print('Esse valor não existe na lista')