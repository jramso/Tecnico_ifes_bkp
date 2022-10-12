s = 0
n = int(input(" inf. n:"))
for i in range(1,n+1):
	num = 2*i-1
	den = n - (i-1)
	if i % 2 == 1:
		s += num/den
	else:
		s -= num/den
print ("A soma é: ",s)