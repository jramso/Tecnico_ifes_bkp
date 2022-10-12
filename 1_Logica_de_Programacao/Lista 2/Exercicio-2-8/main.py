lista=[]
media=0
for i in range (0,5):
  lista.append(int (input('Insira a idade : ')))
  media+=lista[i]

media=media/5

contador=0
for i in range (0,5):
  if lista[i]>13 and lista[i]>media:
    contador+=1
    
print('Quantidades de alunos maior que 13 anos \n e maior que a média são : ', contador)