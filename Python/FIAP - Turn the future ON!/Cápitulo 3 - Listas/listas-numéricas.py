from lista_dentro_de_listas import *

valores = []

for elemento in inventario:
    valores.append(elemento[1])

if len(valores) > 0:
    print("O equipamento mais caro custa:", max(valores))
    print("O equipamento mais barato custa:", min(valores))
    print("O total de equipamentos é de:", sum(valores))


'''
“max()”: que retorna o maior valor numérico dentre os elementos da lista;          
“min()”: que retorna o menor valor numérico dentre os elementos da lista; e          
“sum()”: que retorna o total entre os valores que estão na lista.
'''
