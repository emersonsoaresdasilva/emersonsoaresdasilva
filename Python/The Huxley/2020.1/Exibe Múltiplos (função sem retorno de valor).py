def exibe_multiplos(I,F,X):
    for a in range(I, F + 1):
        if a % X == 0:
            print(a)

I = int(input())
F = int(input())
X = int(input())

exibe_multiplos(I,F,X)