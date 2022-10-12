def areatriangulo():#Exercício 1
  a=float(input("informe um lado do triangulo:"))
  b=float(input("informe outro lado do triangulo:"))

  atri=(a*b)/2
  print('a area do triangulo é:',atri)
f=areatriangulo()

def parimpar():
  c=int(input('inf um numero:'))
  if c%2==0:
    print('o numero',c,'é par')
  else:
    print('o numero',c,'é impar')
f=parimpar()

def impar1ate():
  n=int(input('inf um número:'))
  for i in range(1,n):
    if i%2!=0:
      print(i)
f=impar1ate()

def par1ate():
  n=int(input('inf um número:'))
  for i in range(1,n):
    if i%2==0:
      print(i)
f=par1ate()
