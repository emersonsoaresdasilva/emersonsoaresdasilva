'''
Escreva um programa onde os usuários podem digitar vários números inteiros, um de cada vez. Quando quiser encerrar o programa, basta digitar -1. Nessa hora o programa deverá exibir na tela a média aritmética dos números digitados, com 2 casas decimais.
'''

numeros = []
terminou = False
while not terminou:
    entrada = int(input())
    if entrada == -1:
        terminou = True
    else:
        numeros.append(entrada)

media = 0
for i in range(0, len(numeros)):
    if numeros[i]:
        media += numeros[i] / len(numeros)
print('%.2f'%media)
