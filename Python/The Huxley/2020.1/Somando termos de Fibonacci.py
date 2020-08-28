def fib(N):
     if N==0:
         return 0
     elif N==1:
         return 1
     else:
         return fib(N-1)+fib(N-2)

N = int(input())
Soma = 0
for Contando in range(1,N+1):
    Novo = int(input())
    Soma += fib(Novo)
print(Soma)