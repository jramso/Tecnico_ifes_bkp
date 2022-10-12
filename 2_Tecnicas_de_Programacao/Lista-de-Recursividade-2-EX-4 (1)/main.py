lista=[]
def somval(n):
  if n%2==0 and n>0:
    lista.append(n)
    return somval(n-2)
  else:
    if n>0:
      return somval(n-1)
  print(sum(lista))
