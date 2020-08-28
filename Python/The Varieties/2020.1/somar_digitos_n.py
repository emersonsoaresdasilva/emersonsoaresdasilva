def somar_digitos(n):
    soma = 0
    while n != 0:
        soma += n % 10
        n = int(n / 10)
    return soma

n = int(input())
print(somar_digitos(n))
    
    

