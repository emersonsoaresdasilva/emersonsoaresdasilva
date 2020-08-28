N = int(input())
M = 0

while N >= 10:
    M = M + (N % 10)
    N = N // 10
    M = M * 10
M = M + N
print(M)
