x = int(input())
n = int(input())
valores = []
for _ in range(n): # Guarda os valores lidos na lista
    valores.append(int(input()))
    qtd = valores.count(x)
print(qtd)