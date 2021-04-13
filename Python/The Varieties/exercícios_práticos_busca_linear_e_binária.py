def busca_linear(lista, chave): # O(n)
    # Percorre lista do índice 0 a n–1.
    for i in range(len(lista)):
        if lista[i] == chave:
            # Encontrou elemento na posição i.
            return i
    # Não encontrou o elemento.
    return -1

def busca_binaria(lista, chave): # O(log n)
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            # Encontrou elemento.
            return meio
        elif chave > lista[meio]:
            # Busca na segunda metade da lista.
            inicio = meio + 1
        else:
            # Busca na primeira metade da lista.
            fim = meio - 1
    # Não encontrou o elemento.
    return -1
'''
EXERCÍCIO 1:
Implemente a função 'ordem_crescente' que recebe uma lista e retorna True caso
a lista esteja ordenada em ordem crescente e False caso contrário
'''
def ordem_crescente(lista):
    for i in range(len(lista) -1):
        if lista[i+1] < lista[i]:
            return False
    return True
    # return True if lista == sorted(lista) else False

'''
EXERCÍCIO 2:
Implemente a função 'busca_linear_alteracao', alterando o algoritmo de
busca linear para que ele se torne um algoritmo de atualização.
Caso seja encontrado o elemento chave, ele faz a alteração para um novo valor,
passado por parâmetro.
Deve alterar apenas a primeira ocorrência do valor encontrado.
'''
def busca_linear_alteracao(lista, chave, novo_valor):
    for i in range(len(lista)):
        if lista[i] == chave:
            lista[i] = novo_valor
            return True
    return False
'''
EXERCÍCIO 3:
Implemente a função 'busca_binaria_alteracao', alterando o algoritmo de
busca binária para que ele se torne um algoritmo de atualização.
Caso seja encontrado o elemento chave, ele faz a alteração para um novo valor,
passado por parâmetro.
Deve alterar apenas a primeira ocorrência do valor encontrado.
'''
def busca_binaria_alteracao(lista, chave, novo_valor):
    inicio, fim = 0, len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            lista[meio] = novo_valor
            return True
        elif chave > lista[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False

'''
EXERCÍCIO 4:
Implemente a função 'insere_ordenado', que recebe uma lista ordenada de forma
crescente e um novo item que deve ser inserido na lista, de forma que a lista
continue ordenada.
Você NÃO DEVE utilizar as funções sort, sorted, ou qualquer outra função
pronta do python para ordenação.
'''
def insere_ordenado(lista, item):
    for i in range(len(lista)):
        if lista[i] >= item:
            lista.insert(i, item)
            return True
    # Terminou de percorrer a lista:
    # Todos os valores são menores, então insere no final da lista.
    lista.append(item)

    # if ordem_crescente(lista):
    #     inicio, fim = 0, len(lista)-1
    #     while inicio <= fim:
    #         meio = (inicio + fim) // 2 # Pego o meio da lista.
    #         if item < lista[meio]:
    #             fim = meio - 1
    #         else:
    #             inicio = meio + 1
    #     lista.insert(inicio, item)
    # else:
    #     return 'A lista não está ordenada.'