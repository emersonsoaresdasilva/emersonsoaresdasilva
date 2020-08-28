'''
Variável acumuladora, exemplo: Calcular a soma de 05 números digitados pelo usuário.
'''

Soma = 0
Cont = 1

while Cont <=5:
    Num = int(input('Número: '))
    Soma += Num
    Cont += 1
print('A soma dos números é:', Soma)
