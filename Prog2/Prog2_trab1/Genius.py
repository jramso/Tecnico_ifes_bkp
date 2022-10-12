#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Genius.py
#
#  Copyright 2021
#  Autor: Josué Ramos Souza
#  Matricula: 20202BSI0292
#  
# Este é um arquivo de Programa Python Modularizado que representa
# um jogo popular da década de 80 chamado "Genius" porém
# utilizando números no lugar de cores.
#########################################
#imports

from modulos import *
def main():
  #entrada de dados
  nome=input("informe seu nome:")
  limpaTela()
  jogar(nome,0)

if __name__ == "__main__":
  main()