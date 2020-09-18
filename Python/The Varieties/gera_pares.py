'''
def gera_pares(numero_maximo):
    i = 1
    while i <= numero_maximo:
        if i % 2 == 0:
            print(i)
        i += 1
'''
def gera_pares_lista(numero_maximo): #Ouvidos da função.
    lista = []
    i = 1
    while i <= numero_maximo:
        if i % 2 == 0:
            lista.append(i)
        i += 1
    return lista #Boca da função.

#Programa principal:
maximo = 10
pares = gera_pares_lista(maximo)
print(pares)
