def teste(x):
    if x < 5:
        return 3 * x
    else:
        return 2 * teste(x - 5) + 7

# Qual o valor de retorno para a chamada teste(4)?
# teste(4) = 3 * 4 = 12
# print(teste(4))
# Resposta: 12

# Qual o valor de retorno para a chamada teste(10)?
# teste(10) = 2 * 7 + 7 = 21
# teste(5) = 2 * 0 + 7 = 7
# teste(0) = 3 * 0 = 0
# print(teste(10))
# Resposta: 21

# Qual o valor de retorno para a chamada teste(12)?
# teste(12) = 2 * 19 + 7 = 45
# teste(7) = 2 * 6 + 7 = 19
# teste(2) = 3 * 2 = 6
# print(teste(12))
# Resposta: 45
    
def teste_2(x , Y):
    if x < y:
        return -3
    else:
        return 2 * teste_2(x - y, y + 3) + y

# Qual o valor de retorno para a chamada teste(2, 7)?
# teste(2, 7) = -3
# print(teste_2(x, y))
# Resposta: -3

# Qual o valor de retorno para a chamada teste(5, 3)?
# Pilha de Chamadas Recursivas:
# teste(5, 3) = 2 * teste(5 - 3, 3 + 3) + 3
# teste(2, 6) = -3

# Desempilhamento dos Resultados:
# teste(5, 3) = 2 * -3 + 3 = -3 (Retorno Final: -3)
# teste(2, 6) = -3
# print(teste_2(x, y))
# Resposta: -3

# Qual o valor de retorno para a chamada teste(15, 3)?
# Pilha de Chamadas Recursivas:
# teste(15, 3) = 2 * teste(15 - 3, 3 + 3) + 3
# teste(12, 6) = 2 * teste(12 - 6, 6 + 3) + 6
# teste(6, 9) = -3

# Desempilhamento dos Resultados:
# teste(15, 3) = 2 * 0 + 3 = 3 (Retorno Final: 3)
# teste(12, 6) = 2 * -3 + 6 = 0
# teste(6, 9) = -3
# print(teste_2(x, y))
# Resposta: -3

def teste_3(n):
    if n == 1:
        return -n
    else:
        return -5 * teste_3(n - 1) + n

# Qual o valor de retorno da função, caso n = 4?
# Pilha de Chamadas Recursivas:
# teste(4) = -5 * teste(4 - 1) + 4
# teste(3) = -5 * teste(3 - 1) + 3
# teste(2) = -5 * teste(2 - 1) + 2
# teste(1) = -1

# Desempilhamento dos Resultados:
# teste(4) = -5 * -32 + 4 = 164 (Retorno Final: 164)
# teste(3) = -5 * 7 + 3 = -32
# teste(2) = -5 * -1 + 2 = 7
# teste(1) = -1
# print(teste_3(4))
# Resposta: 164

def funcao(n):
    if n == 1:
        return 1
    else:
        return funcao(n - 1) + 8 * n - 7

# Qual o valor de retorno da função, caso n = 5?
# funcao(5) = 53 + 8 * 5 - 7 = 85
# funcao(4) = 28 + 8 * 4 - 7 = 52
# funcao(3) = 10 + 8 * 3 - 7 = 27
# funcao(2) = 1 + 8 * 2 - 7 = 10
# funcao(1) = 1
# print(funcao(5))
# Resposta: 85

# O máximo divisor comum (MDC) de dos números inteiros x e y é o maior inteiro que é divisível por x e y, e pode pode ser calculado de acordo com a definição abaixo. 
# Escreva uma função recursiva em python que calcule o MDC de dois números inteiros positivos.

def mdc(x, y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return mdc(y, x)
    else:
        return mdc(y, x % y)

# print(mdc(10, 30))
# print(mdc(7, 70))

# Pode-se calcular o resto da divisão de dois números inteiros utilizando a definição abaixo. 
# Escreva uma função recursiva em python que calcule o resto da divisão entre dois números inteiros positivos.

def mod(x, y):
    if x < y:
        return x
    elif x == y:
        return 0
    else:
        return mod(x - y, y)

# print(mod(9, 2))
# print(mod(20, 15))

# Escreva uma função recursiva em python que recebe como entrada um número inteiro positivo N e retorna o somatório de todos os números inteiros no intervalo de 1 a N.

def somatorio(n):
    if n == 0:
        return 0
    else:
        return n + somatorio(n-1)

'''
somatorio(5) = 5 + somatorio(4) = 5 + 10 = 15 (resultado final)
somatorio(4) = 4 + somatorio(3) = 4 + 6 = 10
somatorio(3) = 3 + somatorio(2) = 3 + 3 = 6
somatorio(2) = 2 + somatorio(1) = 2 + 1 = 3
somatorio(1) = 1 + somatorio(0) = 1 + 0 = 1
somatorio(0) = 0
'''

# print(somatorio(5))
# print(somatorio(10)) 

# Escreva uma função recursiva em python que receba dois números inteiros A e B, e calcula o resultado de AB. Considere que o resultado de A^B é igual a A * A^B-1. 
# Por exemplo: o resultado de 45 pode ser calculado como:
# 4^5 = 4 * 4^4
# 4^4 = 4 * 4^3
# 4^3 = 4 * 4^2
# 4^2 = 4 * 4^1
# 4^1 = 4 * 4^0
# 4^0 = 1

def potencia(a, b):
    if b == 0:
        return 1 # Qualquer número elevado a 0, sempre retornará 1.
    else:
        return a * potencia(a, b-1)

# print(potencia(2, 5))
# print(potencia(10, 2))

'''
potencia(2, 5) = 2 * potencia(2, 4) = 2 * 16 = 32 (resultado final)
potencia(2, 4) = 2 * potencia(2, 3) = 2 * 8 = 16
potencia(2, 3) = 2 * potencia(2, 2) = 2 * 4 = 8
potencia(2, 2) = 2 * potencia(2, 1) = 2 * 2 = 4
potencia(2, 1) = 2 * potencia(2, 0) = 2 * 1 = 2
potencia(2, 0) = 1
'''

# Escreva uma versão recursiva do algoritmo de busca linear. O algoritmo deve receber como entrada uma lista e uma chave de busca, e retornar True caso a chave de busca seja localizada, ou False, caso não seja localizada. 

def busca(lista, x):
    if len(lista) == 0:
        return False
    elif lista[0] == x:
        return True
    else:
        return busca(lista[1:], x)

'''
busca([5, 7, 3, 2, 1], 2) = busca([7, 3, 2, 1], 2) = True (resultado final)
busca([7, 3, 2, 1], 2) = busca([3, 2, 1], 2) = True
busca([3, 2, 1], 2) = busca([2, 1], 2) = True
busca([2, 1], 2) = True
'''

# lista = [5, 7, 3, 2, 1]
# print(busca(lista, 2))
# print(busca(lista, 9))
