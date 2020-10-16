#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 06 |
#   Formatação com PEP8 (Trybe)
#-------------------------------------

# pip install flake8
# flake8 formatacao-com-pep8.py

import sys
import os

a = []

b = ('enaduenduaneiun aendanufnofvsn nscudndsusnudnfdio'
     'ofemspmfsmepmfso asimfdi eunsufns')

idade = 19

if idade > 18:
    print('Maior de idade')

print(sys.argv) #Argumentos disponíveis.
print(os.times()) #Tempo de execução do processo.

nome = 'Emerson Soares da Silva'

print(f'Nome: {nome}')
