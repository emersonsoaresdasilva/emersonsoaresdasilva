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
