Quantidade = 0
X, Y = input().split()
X, Y = int(X), int(Y)

for i in range(X):
    Numero = int(input())
    if(Numero==Y):
        Quantidade += 1
print(Quantidade)