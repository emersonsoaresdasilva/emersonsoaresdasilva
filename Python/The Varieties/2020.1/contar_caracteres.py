def contar_caracteres(S):
    cmax = 50
    contagem = len(S)
    if contagem <= cmax:
        return contagem

S = str(input())
print(contar_caracteres(S))

#--------------------
# Versão com while!
#--------------------

'''
def contar_dígitos(N):
    if N < 2: return 1
    C, I = 0, 1
    while I <= N:
        I *= 10
        C += 1
    return C

N = int(input())
print(contar_dígitos(N))
'''
