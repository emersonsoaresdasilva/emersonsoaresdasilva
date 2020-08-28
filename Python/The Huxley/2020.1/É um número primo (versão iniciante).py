def primo(n):
    qtd = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd += 1
    return qtd == 2

n = int(input())
while n != -1:
    if primo(n): print(1)
    else: print(0)
    n = int(input()) 