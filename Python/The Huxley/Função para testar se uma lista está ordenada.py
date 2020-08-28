def lista_ordenada(lista):
    verificar = lista
    if sorted(lista) == verificar:
        return True
    else:
        return False

def main():
	sequencia = eval(input())
	resultado = lista_ordenada(sequencia)
	print(str(resultado))
main()
