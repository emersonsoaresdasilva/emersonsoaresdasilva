'''
Escreva um programa para exbir todos os números pares de 0 até o número
informado pelo usuário.
'''

Limite = int(input())
Numero = 0

while Numero <= Limite:
    if Numero % 2 == 0:
        print(Numero)
    Numero += 1
