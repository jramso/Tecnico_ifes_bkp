listam=[] #matricula
listan=[] #nota
media=0.0 #media das notas 
notaA=0 #notas acima da média 
notabx=0 #notas abaixo da média 

for i in range (0,50):
 listam.append(input('Insira a Matrícula: '))
 listan.append(float(input('Insira a nota: ')))
 
 if listan[i]>60:
   notacima+=1
 if listan[i]<60:
   notabaixo+=1
 media+=listan[i]

print('A média das notas é igual a: ',media/50)
print('Notas acima da média: ',notaA,"\n Notas abaixo da média: ",notabx)

  



