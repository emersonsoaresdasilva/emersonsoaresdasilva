# Ordenação por bolha.
'''
• Um dos algoritmos de ordenação mais lento.
• Implementação simples.
• Recomendado para conjuntos pequenos de dados.
• Funciona através da comparação de elementos dois a dois.
- Consiste em “Borbulhar” o maior elemento para o final da lista.

Procedimento:
- Compare o primeiro elemento com o segundo e troque-os se o primeiro for maior que o segundo
- Compare o segundo elemento com o terceiro e troque-os se o segundo for maior que o terceiro
- Compare o terceiro elemento com o quarto e troque-os se o terceiro for maior que o quarto
- E assim sucessivamente …

Ao final desses passos, o maior elemento estará no final da lista!
Agora precisamos repetir todo esse processo N vezes.
'''
def bubble_sort(lista):
    trocas = 0
    comparacoes = 0
    n = len(lista) # Lista = [5, 3, 2, 1, 90, 6]
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            comparacoes += 1
            if lista[j] > lista[j+1]:   # [5, 3, 2, 1, 90, 6] Compara os dois primeiros elementos da lista.
                aux = lista[j]          # [3, 5, 2, 1, 90, 6] 5 é maior que 3, então troca.
                lista[j] = lista[j+1]   # [3, 5, 2, 1, 90, 6] Compara 5 com o próximo elemento 2.
                lista[j+1] = aux        # [3, 2, 5, 1, 90, 6] 5 é maior que 2, então troca.
                trocas += 1
                                        # [3, 2, 1, 5, 6, 90] ao final da 1ª iteração, o maior estará no final.
                                        # Agora temos que repetir o processo novamente... até ordenar toda lista.
    return f'bubble_sort → foram realizadas: {comparacoes} comparações e {trocas} trocas.'
# Ordenação por Seleção.
'''
• Algoritmo de ordenação lento.
• Implementação simples.
• Recomendado para conjuntos pequenos de dados.

Procedimento:
- Encontre o menor elemento da lista e troque com a primeira posição.
- Encontre o segundo menor elemento da lista e troque com a segunda posição.
- E assim por diante, até que a lista esteja ordenado.

Observação: Quando o elemento já está na posição correta, ele troca por ele mesmo (contabiliza como uma troca).
'''
def selection_sort(lista):
    trocas = 0
    comparacoes = 0
    n = len(lista) # Lista = [70, 90, 1, 3, 0, 100, 2]
    for i in range(0, n-1):
        menor = i
        for j in range(i + 1, n):       # Encontramos o menor elemento: zero.
            comparacoes += 1
            if lista[j] < lista[menor]: # Trocamos com a primeira posição: 70.
                menor = j
        aux = lista[i]                  # Realiza a troca.
        lista[i] = lista[menor]
        lista[menor] = aux
        trocas += 1
    return f'selection_sort → foram realizadas: {comparacoes} comparações e {trocas} trocas.'
# Ordenação por inserção.
'''
• Algoritmo de ordenação lento
• Implementação simples
• Recomendado para conjuntos pequenos de dados

Procedimento:
- Comparar um elemento com todos os elementos à sua esquerda e, se esse elemento for menor, trocar esses elementos de posição 
- Essas comparações e trocas só devem parar quando o elemento for maior que o elemento à sua esquerda ou quando o elemento estiver na primeira posição da lista
'''
def insertion_sort(lista):
    trocas = 0
    comparacoes = 0
    n = len(lista)
    for i in range(1, n):
        j = i
        comparacoes += 1
        while j > 0 and lista[j] < lista[j-1]:
            aux = lista[j]
            lista[j] = lista[j-1]
            lista[j-1] = aux
            j -= 1
            trocas += 1
    return f'insertion_sort → foram realizadas: {comparacoes} comparações e {trocas} trocas.'

# Exercícios Teóricos - Métodos de Ordenação Simples:
'''
1 - O algoritmo de ordenação que encontra o menor elemento e o troca com a primeira posição, depois o segundo menor com a segunda posição, e assim sucessivamente, usa o método de:
Resposta: Selection Sort
 
2 - O algoritmo de ordenação baseado em vários percursos sobre a lista, realizando, quando necessárias, trocas entre pares de elementos consecutivos denomina-se método:
Respota: da bolha (bubble sort)
 
3 - Qual é o tipo de algoritmo de ordenação que tem como princípio percorrer o vetor diversas vezes, a cada passagem fazendo o maior elemento se mover para o final da estrutura?
Resposta: Bubble sort

4 - Dada a sequência numérica [17, 43, 37, 31, 8, 77, 52, 25] para ordenar pelo algoritmo Bubble Sort, qual é a sequência parcialmente ordenada depois de completada a segunda iteração do algoritmo?
Resposta: [17, 31, 8, 37, 43, 25, 52, 77]
 
5 - Ao utilizar o método de ordenação Bubble Sort para ordenar uma lista em ordem crescente contendo os números [10, 8, 7, 0], serão feitas:
Resposta: 6 comparações e 6 trocas.
 
6 - Quantas comparações e trocas de elementos ocorrerão se utilizarmos o algoritmo Bubble Sort para ordenar a lista [60, 32, 45, 5, 6, 2] em ordem crescente:
Resposta: 15 comparações e 13 trocas.

7 - Quantas comparações e trocas de elementos ocorrerão se utilizarmos o algoritmo Bubble Sort para ordenar a lista [31, 11, 23, 17, 13] em ordem crescente:
Resposta: 10 comparações e 7 trocas.

8 - Faça um teste de execução do método bubble sort para a lista a seguir: [30, 40, 50, 20, 10]
• Quantas operações de comparações de elementos foram realizadas?
Resposta: 14 comparações.
• Quantas operações de trocas de elementos foram realizadas?
Resposta: 7 trocas de elementos.

9 - Faça um teste de execução do método selection sort para a lista a seguir: [10, 50, 40, 30, 20]
• Quantas operações de trocas de elementos foram realizadas?
Resposta: 4 trocas.

10 - Preencha uma lista com 1000 números inteiros em ordem decrescente.
lista = list(range(1000, 0, -1))

Na sequência, ordene essa lista utilizando os métodos bubble, selection e insertion sort, e informe, para cada um deles:

• Quantas operações de comparações de elementos foram realizadas?
• Quantas operações de trocas de elementos foram realizadas?

Dica: altere os métodos, inserindo variáveis contadoras para fazer as contagens.

11 - Repita o exercício anterior, agora utilizando uma lista com 1000 números inteiros em ordem crescente.
lista = list(range(0, 1000))
'''
print(f'\n{bubble_sort(lista)}\n{selection_sort(lista)}\n{insertion_sort(lista)}\n')

# # -------------------------------------------------
# lista = [6, 7, 4, 1, 3, 2, 5]
# bubble_sort(lista)
# print(lista)

# lista = [1, 2, 3, 4, 5, 6, 7]
# bubble_sort(lista)
# print(lista)

# lista = [7, 6, 5, 4, 3, 2, 1]
# bubble_sort(lista)
# print(lista)

# # -------------------------------------------------
# lista = [6, 7, 4, 1, 3, 2, 5]
# selection_sort(lista)
# print(lista)

# lista = [1, 2, 3, 4, 5, 6, 7]
# selection_sort(lista)
# print(lista)

# lista = [7, 6, 5, 4, 3, 2, 1]
# selection_sort(lista)
# print(lista)

# # -------------------------------------------------
# lista = [6, 7, 4, 1, 3, 2, 5]
# insertion_sort(lista)
# print(lista)

# lista = [1, 2, 3, 4, 5, 6, 7]
# insertion_sort(lista)
# print(lista)

# lista = [7, 6, 5, 4, 3, 2, 1]
# insertion_sort(lista)
# print(lista)
# # -------------------------------------------------
