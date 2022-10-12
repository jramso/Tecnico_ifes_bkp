import os
import pickle
#função que le um arquivo
def leArquivo(nome):
  arquivo = open(nome,'r')
  print (arquivo.read())
  arquivo.close()
#fim_da_funcao

#função que salva em arquivo
def writeArqBin(chave,info,dicio):
  arq=open('multas.bin','rb')
  motoristas=pickle.load(arq)
  veiculos=pickle.load(arq)
  infracoes=pickle.load(arq)
  naturezas=pickle.load(arq)
  arq.close()
  arq = open("multas.bin",'wb')
  if dicio==motoristas:
    motoristas[chave]=info
  elif dicio==veiculos:
    veiculos[chave]=info
  elif dicio==infracoes:
    infracoes.append(info)
  pickle.dump(motoristas,arq)
  pickle.dump(veiculos,arq)
  pickle.dump(infracoes,arq)
  pickle.dump(naturezas,arq)
  arq.close()

def alteraArqBin(veiculos):
  arq=open('multas.bin','rb')
  motoristas=pickle.load(arq)
  vei=pickle.load(arq)
  infracoes=pickle.load(arq)
  naturezas=pickle.load(arq)
  arq.close()
  arq = open("multas.bin",'wb')
  pickle.dump(motoristas,arq)
  pickle.dump(veiculos,arq)
  pickle.dump(infracoes,arq)
  pickle.dump(naturezas,arq)
  arq.close()



def readArqBin(nome):
  if os.path.isfile("multas.bin"):
    arq=open(nome,'rb')
    ler=pickle.load(arq)
    ler2=pickle.load(arq)
    ler3=pickle.load(arq)
    ler4=pickle.load(arq)
    print(ler)
    print(ler2)
    print(ler3)
    print(ler4)
