lista=[]
troca=0 #variavel para armazenar informação temporária

for i in range(0,20):
 lista.append(int (input('Insira o valor na lista: ')))

for i in range(0,10):
 troca=lista[19-i]
 lista[19-i]=lista[i]
 lista[i]=troca


print(lista)