
n=int (input("Inf o valor de N: "))
m=int (input("Inf o valor de M: "))

cont= 0
for i in range (1,m+1):
  if i%n==0:
    cont=cont+1
   

print("existem ",cont," multiplos de ",n," até ",m) 