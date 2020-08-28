def minimo(numero):
    minimo = numero[0]
    for i in range(1, len(numero)): #[1..7[
        if numero[i] < minimo:
            minimo = numero[i]
    return minimo       

def maximo(numero):
    maximo = numero[0]
    for i in range(1, len(numero)): #[1..7[
        if numero[i] > maximo:
            maximo = numero[i]
    return maximo 
