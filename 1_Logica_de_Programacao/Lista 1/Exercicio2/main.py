n= int(input("informe um número:"))
n2= int(input("informe outro número:"))
n3= int(input("informe outro número:"))

MG= 0
MH= 0
MP= 0
MA= 0

input("""G= geométrica
H= harmônica
P= Ponderada
A= Aritmética
*Nota: se um dos números for negativo é impossivel calcular as médias """)
Tmed=str(input("informe o tipo de média:"))

if n<0:
  print ("não foi possível calcular as médias")
elif n2<0:
  print ("não foi possível calcular as médias")
elif n3<0:
  print ("não foi possível calcular as médias") 
elif Tmed=="G" :
    MG= (n*n2*n3)**(1/3)
    print("média Geométrica",MG)
elif  Tmed=="H":
    MH= 1/((1/n)+(1/n2)+(1/n3))
    print("média Harmônica",MH)
elif Tmed=="P" :
    MP= (n+(2*y)+(3*z))/6
    print("média Ponderada",MP)
elif Tmed=="A" :
    MA= (n+n2+n3)/3
    print("média Aritmética:",MA)


