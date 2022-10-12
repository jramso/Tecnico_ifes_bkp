def algigual(alg,num,cont):
  a=list(str(num))
  b=int(len(a))
  if a[b-1]==str(alg):
    return algigual(alg,num,cont+1)
  else:
    return algigual(alg,num//10,cont)
  print(cont)
  
    