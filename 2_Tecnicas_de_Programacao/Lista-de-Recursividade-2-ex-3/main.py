def listsum(numList):
  if len(numList)==1:
    return numList[0]
  else:
    return numList[0]+listsum(numList[1:])
print(listsum([1,3,5,7,9]))
print('')
print('o resultado é 25 por que ele soma as variaveis de todas as posiçoes da lista')