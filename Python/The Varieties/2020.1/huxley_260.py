# Conta os divisores entre 1 e n.
def primo1(n):
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False

# Conta os divisores entre 1 e n.
def primo2(n):
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    return divisores == 2

# Conta os divisores entre 2 e n-1.
def primo3(n):
    divisores = 0
    for i in range(2, n):
        if n % i == 0:
            divisores += 1
    return n > 1 and divisores == 0

# Termina as tentativas de divisão na
# primeira com resto zero.
def primo4(n):
    if n == 1: return False
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor == n

# Testa apenas divisores ímpares.
def primo5(n):
    if n == 1: return False
    if n % 2 == 0: return n == 2
    divisor = 3
    while n % divisor != 0:
        divisor += 2
    return divisor == n

# Testa divisores até a metade de n.
def primo6(n):
    if n % 2 == 0: return n == 2
    divisor = 3
    metade = n // 2
    while divisor <= metade and n % divisor != 0:
        divisor += 2
    return n > 1 and divisor > metade

# Testa divisores até a raiz de n.
from math import sqrt, ceil

def primo7(n):
    if n % 2 == 0: return n == 2
    divisor = 3
    raiz = ceil(sqrt(n))
    while divisor <= raiz and n % divisor != 0:
        divisor += 2
    return n > 1 and divisor > raiz

n = int(input())
while n != -1:
    print(1 if primo7(n) else 0)
    n = int(input())
