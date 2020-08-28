def contar_caracteres(S):
    cmax = 50
    contagem = len(S)
    if contagem <= cmax:
        return contagem

S = str(input())
print(contar_caracteres(S))