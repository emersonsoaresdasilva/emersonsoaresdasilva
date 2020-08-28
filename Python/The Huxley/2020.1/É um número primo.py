def primo(n):
    qtd = 0
    if n != 2 and n % 2 ==0:
        return False
    for divisor in range(3, n, 2):
        if n % divisor == 0:
            return False
    return n > 1 and qtd == 0

n = int(input())
while n != -1:
    if primo(n): print(1)
    else: print(0)
    n = int(input())