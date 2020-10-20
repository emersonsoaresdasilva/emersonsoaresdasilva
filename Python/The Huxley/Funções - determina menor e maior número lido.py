# Escreva o codigo da funcao le_e_devolve_menor() na sequencia:
def le_e_devolve_menor():
    lista = []
    while True:
        n = int(input())
        if n != -1:
            lista.append(n)
        else:
            break;        
    if lista == []:
        return 0
    else:
        return min(lista)

# Escreva o codigo da funcao le_e_devolve_maior() na sequencia:
def le_e_devolve_maior():
    lista = []
    while True:
        n = int(input())
        if n != -1:
            lista.append(n)
        else:
            break;        
    if lista == []:
        return 0
    else:
        return max(lista)

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
if opcao == 'menor':
	menor = le_e_devolve_menor()
	print(menor)
elif opcao == 'maior':
	maior = le_e_devolve_maior()
	print(maior)
