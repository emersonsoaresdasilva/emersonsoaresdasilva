Binario = int(input('Binário: '))

Decimal = 0
Expoente = 0

while Binario > 0:
    Digito = Binario % 10
    Potencia = 2**Expoente
    Decimal += Digito * Potencia
    Binario = Binario // 10
    Expoente += 1
print('Decimal:',Decimal)
