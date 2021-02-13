f = open('10-números-no-arquivo.txt', 'r')

soma = 0

for numero in f:
    soma += int(numero)
print(soma)
f.close()
