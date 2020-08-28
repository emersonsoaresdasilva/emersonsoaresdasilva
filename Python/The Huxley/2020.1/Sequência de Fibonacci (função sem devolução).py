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