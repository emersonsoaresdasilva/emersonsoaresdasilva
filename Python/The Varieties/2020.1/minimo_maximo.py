'''Crie um programa que recebe como entrada diversos números dados
pelo usuário. Ao final, o programa deverá exibir a soma do menor valor
com o maior.
Obs.: A entrada termina com a leitura do valor -1.
'''
# 1ª Versão (funções prontas da linguagem)
'''
L = []

Valor = float(input('Valor: '))

while Valor != -1:
    L.append(Valor)
    Valor = float(input('Valor: '))
Soma = min(L) + max(L)
print(Soma)
'''
# 2ª Versão (funções criadas pelo programador)

def minimo(numero):
    minimo = numero[0]
    for i in range(1, len(numero)): #[1..7[
        if numero[i] < minimo:
            minimo = numero[i]
    return minimo       

def maximo(numero):
    maximo = numero[0]
    for i in range(1, len(numero)): #[1..7[
        if numero[i] > maximo:
            maximo = numero[i]
    return maximo   
'''
L = []

Valor = float(input('Valor: '))

while Valor != -1:
    L.append(Valor)
    Valor = float(input('Valor: '))
Soma = min(L) + max(L)
print(Soma)
'''
# 3ª Versão (sem utilização de listas)
'''
Valor = float(input('Valor: '))
Minimo = Valor
Maximo = Valor
while Valor != -1:
    if Valor < Minimo:
        Minimo = Valor
    elif Valor > Maximo:
        Maximo = Valor
    Valor = float(input('Valor: '))
Soma = Minimo + Maximo
print(Soma)
'''
