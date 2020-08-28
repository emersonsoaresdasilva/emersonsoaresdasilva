'''Crie um programa que exiba todos os números pares de 8 até 100.'''

# ------------------------------
# Versão com while
# ------------------------------

par = 8
while par <= 100:
    print(par, end=' ')
    par += 2

print('\n\n')

# ------------------------------
# Versão com for
# ------------------------------

for par in range(8, 100+1, 2): # [8..100+1[
    print(par, end=' ')

