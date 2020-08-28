# Validação de dado de entrada.
def entrada():
    n = int(input('Inteiro e positivo: '))
    while n <= 0:
        n = int(input('Inteiro e positivo: '))
    return n

# Quantidade de divisores.
def qtd_divisores(n):
    qtd = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd += 1
    return qtd

x = entrada()
print(x, 'tem', qtd_divisores(x), 'divisores')
