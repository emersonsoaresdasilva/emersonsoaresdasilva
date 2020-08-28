# Devolve a quantidade de divisores de n.
def qtd_divisores(n):
    qtd = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd += 1
    return qtd

# Devolve um valor que indica se n é primo.
def primo(n):
    return qtd_divisores(n) == 2

# Exibe todos os primos do intervalo [a..b].
def intervalo_primos(a, b):
    for num in range(a, b+1): # [a..b+1[
        if not primo(num): print(num, end=' ')

n = int(input())
intervalo_primos(1, n)

'''
n = int(input())

nao_primos = 0
for i in range(1, n+1):
    divisores = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisores +=1
    if divisores != 2:
        print(j, end=' ')
'''
            
