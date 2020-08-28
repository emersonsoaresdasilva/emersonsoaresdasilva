def contar_d�gitos(N):
    if N < 2: return 1
    C, I = 0, 1
    while I <= N:
        I *= 10
        C += 1
    return C

N = int(input())
print(contar_d�gitos(N))