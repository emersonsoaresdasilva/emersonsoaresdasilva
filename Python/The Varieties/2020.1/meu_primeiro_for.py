'''Crie um programa que exiba os 100 primeiros números naturais.'''

# --------------------
# Versão com while
# --------------------

num = 0
while num < 100:
    print(num, end=' ')
    num += 1
print('a variável num é:', num)

print('\n------------------------\n')

# --------------------
# Versão com for
# --------------------

for num in range(100): # [0..100[
    print(num, end=' ')
print('a variável num é:', num)
