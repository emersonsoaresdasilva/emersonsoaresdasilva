def maximo(numero):
    maximo = numero[0]
    for i in range(1, len(numero)): #[1..7[
        if numero[i] > maximo:
            maximo = numero[i]
    return maximo   
    
n = int(input())
i = 0
lista = []
while i < n:
    novo = int(input())
    lista.insert(0,novo)
    i += 1
print(maximo(lista))