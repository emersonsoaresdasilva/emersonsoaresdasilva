#fibonacci(n) = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,  ..., n
#               a  b

def fib(n):
    a = 1
    b = 1
    for i in range(2, n+1):
        b = b + a
        a = b - a
    return a

for i in range(1, 10+1): # Por que dez?
    s = fib(i) # não seria melhor acumular?

print(s) # O que está imprimindo aqui?
