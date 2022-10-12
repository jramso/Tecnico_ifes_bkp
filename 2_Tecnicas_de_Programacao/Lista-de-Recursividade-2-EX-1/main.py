lista=[]
def pot(base,expoente):
  lista.append(base)
  first=int(lista[0])
  if expoente==0:
    return 1
  elif expoente != 1:
    return pot(base*first,expoente-1)
  print(lista[-1])

    