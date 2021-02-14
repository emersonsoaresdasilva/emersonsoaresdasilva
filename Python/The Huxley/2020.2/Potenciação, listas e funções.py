# Escreva a funcao potenciacao_em_lista(lista) abaixo:
def potenciacao_em_lista(lista):
    for i in range(1,len(lista)-1):
        if lista[i] % 2 == 0:
            lista[i] = lista[i]**2
        else:
            lista[i] = lista[i]**3
    return lista

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista = eval(input())
resultado = potenciacao_em_lista(lista)
print(resultado)
