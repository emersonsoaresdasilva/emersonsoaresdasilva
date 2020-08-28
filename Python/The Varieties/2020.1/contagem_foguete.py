'''
Escreva um programa para escrever na tela
a contagem regressiva do lançamento de um
foguete. O programa deve exibir 10,9,8,...,1,0 e Fogo!
'''

Contagem = 10

while Contagem >= 0:
    print(Contagem)
    Contagem = Contagem - 1
print('Fogo!')

#Método com sleep!
'''
from time import sleep

Contagem = 10

while Contagem >= 0:
    print(Contagem)
    Contagem = Contagem - 1
    sleep(1)
print('Fogo!')
'''
