Entrada = input()

Sequencia = int(Entrada.split()[0])

Y = Entrada.split()[1]

Contador = 0

for X in range(Sequencia):
    Numero = input()
    if(Numero==Y):
        Contador += 1
print(Contador)

