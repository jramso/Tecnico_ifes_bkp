import os
from random import randint
#esta função limpa a tela
def limpaTela():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")


#esta função separa os algarismos de um número
def numeros(n):
  lista=[]
  leftn=0
  totaln= len(str(n))
  #processamento
  #pega o dígito mais a esquerda
  while totaln != 0:
   leftn=n//(10**(totaln-1))
   totaln = totaln-1
   n=n-(leftn *(10**totaln))
   lista.append(leftn)
  return lista
#fim_da_funcao

#esta função le e exibe o conteudo de um um arquivo
def leArquivo(nome):
  arquivo = open(nome,'r')
  print (arquivo.read())
  arquivo.close()
#fim_da_funcao

#esta função escreve um conteudo dentro de um arquivo
def escreverArquivo(nome,texto):
  old=''
  if os.path.isfile(nome):
    arquivo = open(nome,'r')
    old = (arquivo.read())
  arquivo = open(nome,'w')
  arquivo.write(old)
  arquivo.write(texto)
  arquivo.close()
#fim_da_funcao

#Esta função lê o arquivo de pontos e exibe o usuario com maior pontuação
def listaPontuacao():
  arquivo = open("score.txt",'r')
  linha = arquivo.readline()
  maior=0
  while linha:
    valores = linha.split()
    valorAtual = int(valores[2]) #variavel que pega a pontuacao atual
    if valorAtual > maior:
      maior=int(valores[2]) #variavel da maior pontuacao
      nomeMaior=valores[0]
    #print( valores[0],valores[1], valores[2] )
    linha = arquivo.readline()
  print("a maior pontuação foi do(a) %s com o total de %i pontos:"%(nomeMaior,maior))
  arquivo.close()
#fim da função

#esta é a função em que o jogo acontece ela recebe como parametros o nome de um jogador e seus pontos.
def jogar(nome,pontos):
  x=0
  sorteado = 0 #numeros 'sorteados'
  correta = [] #lista de numeros sorteados
  sequencia = [] #lista de numeros digitados

  #Entrada de dados
  leArquivo("inicio.txt") #arquivo de inicio de jogo
  sorteado = randint(0,9)
  correta.append(sorteado)
  pontuacao="%s , Pontos: %i \n"%(nome,len(correta))  

  #saida de dados 
  print("o primeiro número sorteado foi:",sorteado)
  
  #entrada de dados
  x = int(input("digite a sequencia completa:"))
  sequencia = numeros(x) #lista de numeros da sequencia digitada x

  #processamento
  while sequencia == correta:
    sorteado = randint(0,9)
    correta.append(sorteado)
    limpaTela()
    #saida de dados
    print("o novo número é:", sorteado)
    #entrada de dados
    x=int(input("Digite a sequencia completa:"))
    sequencia = numeros(x)

  #saida de dados
  #processamento
  #Este é o comando condicional que marca o máximo de pontos da sessão
  if pontos<len(correta)-1:
    pontos=len(correta)-1
  #saída de dados
  print("Errou! Você acertou", len(correta)-1,"números.")
  #entrada de dados
  sair=input("deseja sair (S/N)?")
  if sair =='n' or sair=='N':
    limpaTela()
    return jogar(nome,pontos)
  elif sair =='s' or sair=='S':
    pontuacao="%s, Pontos: %i \n"%(nome,pontos)
    escreverArquivo('score.txt',pontuacao)
    print("a maior pontuação alcançada por você nesta sessão é:",pontos)
    listaPontuacao()

#fim da função