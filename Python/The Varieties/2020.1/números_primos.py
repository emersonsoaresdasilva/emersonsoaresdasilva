'''Elabore um fluxograma que verifica se um número natural é primo.'''

#Primeira versão do programa - Método do Professor!
'''
N = int(input('N: '))

Divisores = 0
Denominador = 1

while Denominador <= N:
    if N % Denominador == 0:
        Divisores += 1
    Denominador +=1
if Divisores == 2:
    print('O número é primo')
else:
    print('O número não é primo')
'''
#Segunda versão do programa - Método do colega Wagner!
'''
num = int(input())
qtd = 0
cont = 1
while cont <= num:
    verif = num % cont
    cont += 1
    if verif == 0:
        qtd += 1
if qtd == 2:
    print('Número é primo!')
else:
    print('Número não é primo!')
'''

#Terceira versão do programa - Método do Professor (Função)!
'''
def numero_primo(N):

    Divisores = 0
    Denominador = 1

    while Denominador <= N:
        if N % Denominador == 0:
            Divisores += 1
        Denominador +=1
    if Divisores == 2:
        print('O número é primo')
    else:
        print('O número não é primo')
    return
'''

#Quarta versão do programa - Método do Professor (Função - Return "Sem imprimir")!
def numero_primo(N):

    Divisores = 0
    Denominador = 1

    while Denominador <= N:
        if N % Denominador == 0:
            Divisores += 1
        Denominador +=1
    if Divisores == 2:
        return 'O número é primo'
    else:
        return 'O número não é primo'
    return
