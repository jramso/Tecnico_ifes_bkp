import numpy
matriz=[]
matriz2=[]
matriz3=[]
p1=   ["    pilha 1    "]
p2=   ["    pilha 2    "]
p3=   ["    pilha 3    "]
topo= ["       |       "]
base= ["_______|_______"]
peca1=["    [' 1 ']    "]
peca2=["   ['  2  ']   "]
peca3=["  ['   3   ']  "]
peca4=[" ['    4    '] "]
peca5=["['     5     ']"]

pecavazia=["       |       "]

peca21=["       |       "]
peca22=["       |       "]
peca23=["       |       "]
peca24=["       |       "]
peca25=["       |       "]

peca31=["       |       "]
peca32=["       |       "]
peca33=["       |       "]
peca34=["       |       "]
peca35=["       |       "]
def interface():
  pecas=int(input('Com quantas peças você quer jogar? (nota:no mínimo 3 máx 5):'))
  if pecas<3 or pecas>5:
    print('\n *informe um número de peças válido* \n')
    return interface()
  elif pecas==3:
    matriz=[topo,peca1,peca2,peca3,base,p1]
    matriz2=[topo,peca21,peca22,peca23,base,p2]
    matriz3=[topo,peca31,peca32,peca33,base,p3]
    organize=numpy.matrix(matriz)
    organize2=numpy.matrix(matriz2)
    organize3=numpy.matrix(matriz3)

  elif pecas==4:
    matriz=[topo,peca1,peca2,peca3,peca4,base]
    matriz2=[topo,peca21,peca22,peca23,base]
    organize=numpy.matrix(matriz)
    organize2=numpy.matrix(matriz2)

  elif pecas==5:
    matriz=[topo,peca1,peca2,peca3,peca4,peca5,base]
    matriz2=[topo,peca21,peca22,peca23,peca24,base]
    organize=numpy.matrix(matriz)
    organize2=numpy.matrix(matriz2)
  print('\n',str(organize)[1:-1],'\n \n',str(organize2)[1:-1],'\n\n',str(organize3)[1:-1])   

interface()

def move():
  mova=int(input('escolha a peça que deseja mover:'))
  onde=int(input('pra que pilha deseja mover? (1,2 ou 3)'))
  leiam2=len(matriz2)
  leiam3=len(matriz3)
  if move==1:
    if onde ==1:
      return move()
    elif onde==2:
      ultima=leiam2-1
      #matriz2[]==peca1
      peca1=pecavazia
    print(matriz2)
    
move()
