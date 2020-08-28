def exibe_multiplos(I,F,X):
    for a in range(I, F + 1):
        if a % X == 0:
            print(a)

I = int(input())
F = int(input())
X = int(input())

exibe_multiplos(I,F,X)

#Múltiplos de N num Intervalo!
'''
N = int(input())
A = int(input())
B = int(input())
for i in range(A, B + 1):
    if i % N == 0:
        print (i)
if N > B:
    print ('INEXISTENTE')
'''
