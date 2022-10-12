# def fatorial(n):
#   if n==0:
#     return 1
#   return fatorial(n-1)*n

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  APNP21.py
#
#  Copyright 2021
#  Autor: Josué Ramos Souza
#  Matricula: 20202BSI0292
#  
# Este é arquivo de programa Python Modularizado
# que recebe um valor n e calcula o seu fatorial 
#########################################

#Esta é a função que calcula o fatorial
def fatorial(n):
  #declaração de variaveis
  fat=int(0)
  #inicialização de variaveis
  fat=1
  #processamento
  for i in range(n,0,-1):
    fat=fat*i
  #retorno de dados
  return fat

#Esta é a função principal
def main():
  #declaração de variaveis
  n=int(0)
  #inicialização e entrada de dados
  n=int(input())
  #processamento
  while n>=0:
    resultado=fatorial(n)
    #saída de dados
    print ("Fatorial(%i)=%i"%(n,resultado))
    #entrada de dados
    n=int(input())
#identificação da função main() como a principal
#que está executando o código.
if __name__ == "__main__":
  main()