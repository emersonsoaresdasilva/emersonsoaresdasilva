#Fibonacci(n) = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,  ..., N.
    
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

#Fibonacci versão simples - while!
'''
N = int(input())

Ultimo = 1
Proximo = 0
Contando = 0

while Contando < N:
    print(Ultimo)
    Novo = Ultimo + Proximo
    Proximo = Ultimo
    Ultimo = Novo
    Contando += 1
'''
#Somando numeros de uma sequência.
#Entrada exemplo: 3(Quantidade de termos) 5 8 10 = 23 (saída)
#                                        T1 T2 T3 = 23 (saída)
'''
N = int(input('Quantidade de termos: '))
Contando = 1
Soma = 0
for Contando in range(N):
   Novo = int(input('Termo: ')) 
   Soma += Novo
   Contando += 1
print('Soma dos termos é:',Soma)
'''
