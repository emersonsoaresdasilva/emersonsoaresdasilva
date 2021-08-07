# Escreva a funcao devolve_lista_numeros(x, y) abaixo:
def devolve_lista_numeros(x,y):
    numeros = []
    while x != y + 1:
        numeros.append(y)
        j = y - 1
        y = j
    numeros.sort()
    return numeros

# PROGRAMA PRINCIPAL: nao altere o codigo a partir deste ponto
def programa_principal():
	a = int(input())
	b = int(input())
	resultado = devolve_lista_numeros(a, b)
	print(resultado)
programa_principal()
