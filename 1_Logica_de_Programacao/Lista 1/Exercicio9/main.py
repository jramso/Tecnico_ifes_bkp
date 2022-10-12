SM=0
n= int(input(" Informe o primeiro número: "))
m = int(input(" Informe o segundo número: "))
for x in range(n,m):
	if x % 5 == 0 or x % 11 == 0:
		SM=SM+x
	if x % 5==0 and x % 11 == 0:	
		print(x)
print("Soma dos múltiplos de 5 ou 11 é:",SM)