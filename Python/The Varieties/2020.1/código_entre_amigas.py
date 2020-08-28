'''
Não precisa transformar o código em uma lista, pois strings podem ser indexadas
por posição (primeiro caractere está no índice zero, o segundo no índice 1, etc)
E como as posições do código coincidem com esses índices, você pode usá-los
diretamente.

Quanto às entradas,
cada linha possui vários números,
então você deve iterar pelos números e pegar o caractere correspondente a cada
posição:
'''
#---------------------------------------
#     VERSÃO PROGRAMA PRINCIPAL
#---------------------------------------
'''
codigo = ' abcdefghijklmnopqrstuvwxyz'
while True:
    numeros = input().split()
    palavra = ''
    for n in numeros:
        n = int(n)
        if 0 <= n < len(codigo):
            palavra += codigo[n]
    if palavra == 'fim':
        break
    print(palavra)
'''
'''
O while vai lendo as entradas indefinidamente.
Se a palavra decodificada for "fim", o loop se encerra.
'''

#---------------------------------------
#            VERSÃO FUNÇÃO
#---------------------------------------
'''
codigo = ' abcdefghijklmnopqrstuvwxyz'

def traduzir(numeros):
    palavra = ''
    for n in numeros:
        n = int(n)
        if 0 <= n < len(codigo):
            palavra += codigo[n]
    return palavra

while True:
    numeros = input().split()
    palavra = traduzir(numeros)
    if palavra == 'fim':
        break
    print(palavra)
'''
#---------------------------------------
#      VERSÃO FUNÇÃO PROFESSOR
#---------------------------------------
def converter(codigo):
    for indice in range(len(codigo)):
        codigo[indice] = int(codigo[indice])
    return codigo

def traduzir(codigo):
    codigo = converter(codigo)
    frase = ''
    for indice in range(len(codigo)):
        letra = codigo[indice]
        if letra != 0:
            frase += chr(codigo[indice] + 96)
        else:
            frase += ' '
    return frase

codigo = input().split()
frase = traduzir(codigo)

while frase != 'fim':
    print(frase)
    codigo = input().split()
    frase = traduzir(codigo)
