lista=[]

for i in range(0,50):
  lista.append(float(input('Insira o valor : ')))

maior=0.0
indice=0

for i in range(0,50):
 if maior<lista[i] or i==0:
   maior=lista[i]
   indice=i

print('O maior valor da lista é ',maior,' e está \n na posição ',indice,' da lista ')  