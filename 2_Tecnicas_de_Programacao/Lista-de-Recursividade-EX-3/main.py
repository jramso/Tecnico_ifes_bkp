def regressiva(n):
  print(n)
  if n!=1:
    return regressiva(n-1)
  else:
    return print('Fogo!')
regressiva(int(input("informe um número:")))