'''
L = [100,200,300,400,500]
qtd = 0
x = 100

for i in range(len(L)):
    if L [i]==x:
        qtd +=1

'''
'''

#Método utilizado sem listas!
X = int(input())
N = int(input())
Quantidade = 0
for _ in range(N):
    if int(input()) == X:
        Quantidade += 1
print(Quantidade)
'''
'''
x = int(input())
n = int(input())
valores = []
for _ in range(n): # Guarda os valores lidos na lista
    valores.append(int(input()))
    qtd = valores.count(x)
print(qtd)
'''
def ocorre(x,n):
    qtd = 0
    for num in valores: # percorre a lista e verifica quais são iguais a x
        if num == x:
            qtd += 1
    return qtd

x = int(input())
n = int(input())

valores = []
for _ in range(n): # guarda os valores lidos na lista
    valores.append(int(input()))
print(ocorre(x,n))
