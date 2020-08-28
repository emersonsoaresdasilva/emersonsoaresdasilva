'''A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, ... Escreva um programa
que apresente a série de Fibonacci até o n-ésimo termo (n > 0).
'''
'''
A = 1
B = 1
N = int(input('Digite um número natural: '))
C = 0

for C in range(N):
    print(A, end=' ')
    B = B + A
    A = B - A
'''
'''
A = 1
B = 1

N = int(input('Digite um número natural: '))

C = 0

while C < N:
    print(A, end=' ')
    B = B + A
    A = B - A
    C += 1
'''
def fibonacci(N):
    A = 1
    B = 1
    C = 0
    for C in range(N):
        print(A)
        B = B + A
        A = B - A
        

N = int(input())
fibonacci(N)

