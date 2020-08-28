lista = []
while True:
    n = int(input())
    if n == 0:
        break;
    lista.append(n)
    media = int(sum(lista) / len(lista))
print(media)