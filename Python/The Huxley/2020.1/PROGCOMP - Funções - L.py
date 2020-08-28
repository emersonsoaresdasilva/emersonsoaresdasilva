def ocorre(x,n):
    qtd = 0
    for num in valores:
        if num == x:
            qtd += 1
    return qtd

x = int(input())
n = int(input())

valores = []
for _ in range(n): # guarda os valores lidos na lista
    valores.append(int(input()))
print(ocorre(x,n))