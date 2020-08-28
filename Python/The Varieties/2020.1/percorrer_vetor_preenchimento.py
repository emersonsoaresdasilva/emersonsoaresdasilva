#-------------------
# Versão com while!
#-------------------

idades = 7 * [0]
pos = 0
while pos < 7:
    print('Digite o valor da posição',pos)
    idades[pos] = int(input('Idades: '))
    pos += 1

#-------------------
# Versão com for!
#-------------------

idades = 7 * [0]
for pos in range(len(idades)):
    print('Digite o valor da posição',pos)
    idades[pos] = int(input('Idades: '))
