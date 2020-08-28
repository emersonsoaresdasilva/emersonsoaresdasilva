def menor_zero(N):
    if N < 0:
        return 'menor'
    else:
        return 'nao menor'

N = int(input())
print(menor_zero(N))