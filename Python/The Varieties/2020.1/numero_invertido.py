'''
Escreva um programa ler um número inteiro n, que não contém dígito 0,
e escrever um número inteiro m que corresponde ao número n invertido.
Por exemplo, se n igual a 123, a saída será m igual a 321.
'''

N = int(input())

while(N >= 10): #Enquanto há dois dígitos.
    print(N % 10)
    N = N // 10
print(N)

'''
def exibe_invertido(n):
    while(N >= 10): #Enquanto há dois dígitos.
        print(N % 10)
        N = N // 10
    print(N)
    return

N = int(input())
exibe_invertido(n)
'''

    
