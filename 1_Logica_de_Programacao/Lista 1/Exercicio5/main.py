print("Este programa calcula 20 termos de S")
N=1 
D=2
S=0
for x in range (0,20):
 if x%2==0:
   S= S+(N/D)
   print('s= +',N,'/',D)
 else: 
   S=S-(N/D)
   print('s= -',N,'/',D)
 N=(N+2)
 D=(D*2)
  
print('o Valor de S é = ',S)