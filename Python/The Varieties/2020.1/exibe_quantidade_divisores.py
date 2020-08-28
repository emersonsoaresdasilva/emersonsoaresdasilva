# Programa que exibe a quantidade de divisores de um número
# inteiro positivo
# Validação do dado de entrada.
'''
n = int(input('Digite um número inteiro e positivo: '))
while n <= 0:
    n = int(input('Digite um número inteiro e positivo: '))
    
# Contagem dos divisores do número lido.
# Quantidade de divisores.
qtd = 0
for divisor in range(1, n+1):
    resto = n % divisor
    if resto == 0:
        qtd = qtd + 1
print('%d tem %d divisores' % (n, qtd))
'''
'''
def entrada():
    n = int(input('Digite um número inteiro e positivo: '))
    while n <= 0:
        n = int(input('Digite um número inteiro e positivo: '))
    return n
'''

#Escreva uma função que receba como parâmetro um número inteiro e positivo n e retorne um
#valor booleano indicando se n é primo. Esta função deve usar a função do exercício anterior.

def qtd_divisores(n):
    qtd = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd += 1
    return qtd

def primo(n):
    return qtd_divisores(n) == 2

#Escreva uma função que receba como parâmetro dois números inteiros positivos a e b, com
#(a ≤ b) e exiba em ordem crescente todos os números primos do intervalo fechado [a,b].
#Sua função deve usar necessariamente a função que conta divisores e a função que verifica se
#um número é primo.

def intervalo_primos_for(a, b):
    for num in range(a, b+1):
        if primo(num):
            print(num)

def intervalo_primos_while(a, b):
    num = a
    while num <= b:
        p = primo(num)
        if p:
            print(num)
        num += 1

#Escreva uma função que receba como parâmetro dois números inteiros positivos a e b (a ≤ b)
#e retorne a soma dos números primos no intervalo fechado [a, b]. Sua função deve usar
#necessariamente a função que conta divisores e a função que verifica se um número é primo.

def soma_primos_while(a, b):
    num = a
    soma = 0
    while num <= b:
        p = primo(num)
        if p:
            soma += num
        num += 1
    return soma

def soma_primos_for(a, b):
    soma = 0
    for num in range(a, b+1):
        if primo(num): soma += num
    return soma
