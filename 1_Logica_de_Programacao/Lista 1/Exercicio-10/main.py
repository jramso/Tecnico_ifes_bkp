m = 0 #contador masculino
f = 0  #contador feminino
somage = 0 #somaidades
maior = 0 #idade da pessoa mais velha
for i in range(0,20):
	nome = input(" Inf. nome: ")
	age = int(input(" Inf. idade: "))
	sex = input(" Inf. sexo (M/F): ")
	if sex=='M':
		m += 1
		somage += age 
	else:
		f += 1
	if (age>maior):
		maior = age
		old = nome
if m>0:
	mid = somage/m
else:
	mid = 0

print(' Masculino: ',m,' , Feminino: ',f)
print('Média idade dos homens: ',mid)
print('Mais velho: ',old)