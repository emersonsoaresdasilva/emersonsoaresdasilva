'''
Escrever um algoritmo que lê 5 valores para "a", um de cada vez, e conta quantos destes são negativos, escrevendo esta informação.
'''
j = 0
i = 0
while i < 5:
    a = float(input('\nDigite um valor: '))
    if a < 0.00:
        j += 1
    i += 1
print(f'\nForam digitados {j} numeros negativos')
