def media_valores(N):
    return sum(L) / N

N = int(input())
L = N * [0]
i = 0

while i < N:
    novo = int(input())
    L.insert(0,novo)
    L.sort()
    i += 1
print('%.2f'%media_valores(N))