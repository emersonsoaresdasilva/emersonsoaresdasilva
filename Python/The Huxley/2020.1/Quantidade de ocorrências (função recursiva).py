def contar_digitos(X):
    contagem = X.count(N)
    return contagem

X, N = input().split()

X = str(X)
N = str(N)

print(contar_digitos(X))