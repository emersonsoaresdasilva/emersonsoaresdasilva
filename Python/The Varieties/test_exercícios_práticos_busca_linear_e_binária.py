'''
Esse é um arquivo de teste para o exercício.
Esse arquivo não garante que a solução do exercício esteja correta, pois isso
depende da lógica utilizada na implemnetação de cada função.
Então, mesmo que o resultado da função esteja de acordo com o teste, a
implementação pode não estar atendendo ao objetivo do exercício.
'''

from exercícios_práticos_busca_linear_e_binária import busca_linear_alteracao, busca_binaria_alteracao
from exercícios_práticos_busca_linear_e_binária import ordem_crescente, insere_ordenado

try:
    assert ordem_crescente([1]) is True
    assert ordem_crescente([1, 2]) is True
    assert ordem_crescente([2, 1]) is False
    assert ordem_crescente([1, 2, 3, 4, 5, 6]) is True
    assert ordem_crescente([1, 2, 3, 4, 4, 7]) is True
    assert ordem_crescente([1, 2, 4, 3, 5, 6]) is False
    assert ordem_crescente([6, 5, 4, 3, 2, 1]) is False
    print("CORRETO - Função ordem_crescente")
except AssertionError:
    print("ERRADO  - Função ordem_crescente")
except Exception:
    print("ERRADO  - Função ordem_crescente")

try:
    lista = [1]
    busca_linear_alteracao(lista, 1, 50)
    assert lista == [50]
    lista = [1, 2, 3, 4, 5, 6]
    busca_linear_alteracao(lista, 4, 100)
    assert lista == [1, 2, 3, 100, 5, 6]
    lista = [1, 2, 3, 4, 5, 6]
    busca_linear_alteracao(lista, 10, 100)
    assert lista == [1, 2, 3, 4, 5, 6]
    lista = [1, 4, 3, 4, 5, 4]
    busca_linear_alteracao(lista, 4, 100)
    assert lista == [1, 100, 3, 4, 5, 4]
    print("CORRETO - Função busca_linear_alteracao")
except AssertionError:
    print("ERRADO  - Função busca_linear_alteracao")
except Exception:
    print("ERRADO  - Função busca_linear_alteracao")

try:
    lista = [1]
    busca_binaria_alteracao(lista, 1, 50)
    assert lista == [50]
    lista = [1, 2, 3, 4, 5, 6]
    busca_binaria_alteracao(lista, 4, 100)
    assert lista == [1, 2, 3, 100, 5, 6]
    lista = [1, 2, 3, 4, 5, 6]
    busca_binaria_alteracao(lista, 10, 100)
    assert lista == [1, 2, 3, 4, 5, 6]
    lista = [1, 4, 3, 4, 5, 4]
    busca_binaria_alteracao(lista, 4, 100)
    assert lista == [1, 4, 3, 100, 5, 4]
    print("CORRETO - Função busca_binaria_alteracao")
except AssertionError:
    print("ERRADO  - Função busca_binaria_alteracao")
except Exception:
    print("ERRADO  - Função busca_binaria_alteracao")

try:
    lista = []
    insere_ordenado(lista, 5)
    assert lista == [5]
    lista = [10]
    insere_ordenado(lista, 5)
    assert lista == [5, 10]
    lista = [1, 2, 3, 4, 6, 7]
    insere_ordenado(lista, 5)
    assert lista == [1, 2, 3, 4, 5, 6, 7]
    lista = [1, 2, 3, 4, 5, 5, 6, 7]
    insere_ordenado(lista, 5)
    assert lista == [1, 2, 3, 4, 5, 5, 5, 6, 7]
    lista = [1, 2, 3, 4, 6, 7]
    insere_ordenado(lista, 10)
    assert lista == [1, 2, 3, 4, 6, 7, 10]
    lista = [1, 2, 3, 4, 6, 7]
    insere_ordenado(lista, -1)
    assert lista == [-1, 1, 2, 3, 4, 6, 7]
    print("CORRETO - Função insere_ordenado")
except AssertionError:
    print("ERRADO  - Função insere_ordenado")
except Exception:
    print("ERRADO  - Função insere_ordenado")
