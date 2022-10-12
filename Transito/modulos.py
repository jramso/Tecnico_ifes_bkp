from funcoesarq import *
from pickle import dumps,loads
import os

def limpaTela():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
# Função que administra as opções de operações do sistema
def menu():
  leArquivo("inicio.txt")
  opcao=int(input("Informe o número da operação:"))
  escolha(opcao)

def escolha(caso):

  if os.path.isfile("multas.bin"):
    arq=open('multas.bin','rb')
    motoristas=pickle.load(arq)
    veiculos=pickle.load(arq)
    infracoes=pickle.load(arq)
    naturezas=pickle.load(arq)
    arq.close()
  else:
    #Se nao existir multas.bin cria multas.bin e escreve os dicionarios vazios no arquivo
    #Só para caso de teste
    motoristas={}
    veiculos={}
    infracoes=[]
    naturezas={}
    arq=open('multas.bin','wb')
    pickle.dump(motoristas,arq)
    pickle.dump(veiculos,arq)
    pickle.dump(infracoes,arq)
    pickle.dump(naturezas,arq)
    arq.close()
    return escolha(caso)
  if caso == 1:
    cadastraMotorista(motoristas)
  elif caso == 2:
    cadastraVeiculo(veiculos)
  elif caso == 3:
    alterarProp(veiculos,motoristas)
  elif caso == 4:
    cadastraInfra(infracoes,veiculos,naturezas)
  elif caso == 5:
    limpaTela()
    return leArquivo('fim.txt')
  else:
    print("\nInforme uma operação valida")
  return menu()

#Esta função cadastra novos motoristas
def cadastraMotorista(motoristas):
  #Declaração de variaveis
  dia=0
  mes=0
  ano=0
  #entrada de dados
  cnh=(input("informe os numeros da CNH do motorista:"))
  if cnh in motoristas:
    print("-"*40,"\nEsta CNH ja está cadastrada\n","-"*39)
    return cadastraMotorista(motoristas)
  else:
    nome=input("informe o nome do motorista:")
    data=input("informe a data de vencimento da CNH no formato DD/MM/AAAA: ")
    #Processamento
    datasave=tratarData(data)
    dados=(nome,datasave)
    writeArqBin(cnh,(nome,datasave),motoristas)
  limpaTela()
  print("Motorista Cadastrado com Sucesso!\n")
  
#Esta função cadastra novos veiculos
def cadastraVeiculo(veiculos):
  #Entrada de dados
  placa=input("informe a placa do veículo: ")
  cnh=(input("informe a CNH do proprietário: "))
  model=input("informe o modelo do veículo: ")
  cor=input("informe a cor do veiculo: ")
  #processamento
  if placa in veiculos:
    print ("Esta placa ja está cadastrada")
    return cadastraVeiculo(veiculos)
  else:
    #saida - escrita no arquivo
    writeArqBin(placa,(cnh,model,cor),veiculos)
    limpaTela()
    print("Veículo Cadastrado com Sucesso!\n")

#Esta função altera o proprietario de um veiculo
def alterarProp(veiculos,motoristas):
  #saida de dados
  print("Você deseja alterar o proprietário de um veiculo?\n  Por favor nos forneca algumas informacoes:")
  #entrada de dados
  placa=input("informe a placa do veiculo:")
  #processamento
  if placa in veiculos:
    #entrada de dados
    cnh=input("informe a CNH do novo proprietario:")
    if cnh in motoristas:
      nova=(cnh,veiculos[placa][1],veiculos[placa][2])
      veiculos.pop(placa)
      veiculos[placa]=nova
      print(veiculos)
      #saida de dados - alteração no arquivo
      alteraArqBin(veiculos)
      limpaTela()
      print("Alterado com Sucesso!\n")
  else:
    limpaTela()
    print("*"*40,"\nEssa placa ainda não foi cadastrada!\n","*"*40)

def cadastraInfra(infracoes,veiculos,naturezas):
  natu=(list(naturezas.keys()))#lista com nome perfeito das naturezas
  data=input("informe a data da infração no formato DD/MM/AAAA: ")
  datasave=tratarData(data)
  placa=input("informe a placa do veículo:")
  infra=int(input("Digite 1 para infração leve\nDigite 2 para infração média\nDigite 3 para infração grave\nDigite 4 para infração gravíssimia:\n"))
  numInfra=len(infracoes)+1 #numero da infracao atual
  if placa in veiculos:
    info=(numInfra,datasave,placa,natu[infra-1])
    writeArqBin(0,info,infracoes)
    limpaTela()
    print("Infração Cadastrada com Sucesso!\n")
  else:
    limpaTela()
    print("*"*40," \n Esta placa não está cadastrada no Sistema!\n","*"*40)
   


  

#Esta função faz o tratamento da data em uma tupla
def tratarData(data):
  try:
    dia,mes,ano=map(int, data.split('/'))
  except ValueError:
    print("Por favor informe a data corretamente no formato DD/MM/AAAA, Ex: 01/01/1990")
    data=input("informe a data no formato DD/MM/AAAA:")
    dia,mes,ano=map(int, data.split('/'))
  except:
    print("A data não foi informada corretamente")
    dia=int(input("informe o dia:"))
    mes=int(input("informe o mes:"))
    ano=int(input("informe o ano:"))
  if len(str(ano))<3:
    ano+=2000
  datasave=(dia,mes,ano)
  return datasave
#Fim da funcao