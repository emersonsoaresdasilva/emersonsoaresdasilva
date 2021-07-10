# Classe que representa os nós da Árvore Binária de Busca (BST)
# Uma árvore é constituída por vários nós.
# Cada nó contém um valor, e referências a dois outros nós (esquerda e direita)
class Tree:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return str(self.valor)


# Inserir um novo nó na árvore
def inserir(raiz, valor):
    nodo = Tree(valor)                  # Cria um novo nó
    if raiz is None:                    # Nó é inserido na raiz.
        raiz = nodo
    elif nodo.valor >= raiz.valor:       # Nó é inserido na subárvore direita
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            inserir(raiz.direita, nodo.valor)
    else:                               # Nó é inserido na subárvore esquerda
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            inserir(raiz.esquerda, nodo.valor)


# Pré-Ordem: imprime primeiro o conteúdo da raiz, em seguida imprime toda a
# subárvore esquerda e finalmente imprime toda a subárvore direita
def pre_ordem(raiz):
    if raiz is None:
        return
    print(raiz.valor, end=' ')
    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)


# Simétrica: imprime toda a subárvore esquerda, em seguida imprime o conteúdo
# da raiz e finalmente imprime toda a subárvore direita
def simetrica(raiz):
    if raiz is None:
        return
    simetrica(raiz.esquerda)
    print(raiz.valor, end=' ')
    simetrica(raiz.direita)


# Pós-Ordem: imprime toda a subárvore esquerda, em seguida imprime toda a
# subárvore direita e finalmente imprime o conteúdo da raiz
def pos_ordem(raiz):
    if raiz is None:
        return
    pos_ordem(raiz.esquerda)
    pos_ordem(raiz.direita)
    print(raiz.valor, end=' ')


# Se percorrermos uma árvore de forma simétrica e acompanharmos em qual nível
# na árvore estamos, podemos gerar uma representação gráfica da árvore.
# O parâmetro nível registra onde estamos na árvore. Por ‘default’, o nível
# inicialmente é zero. A cada chamada recursiva repassamos nivel+1 porque o
# nível do filho é sempre # um a mais do que o nível do pai.
# Cada item é indentado quatro espaços por nível.
# A arvore é exibida "deitada", com a raiz à esquerda.
def imprimir(raiz, level=0):
    if raiz is None:
        return
    imprimir(raiz.direita, level+1)
    print('    '*level + str(raiz.valor))
    imprimir(raiz.esquerda, level+1)


# EXERCÍCIOS:

# 1 - Escreva uma função para determinar o número de nós em uma árvore binária
def quantidade(raiz, n=0):
    if raiz is None:
        return 0
    return quantidade(raiz.esquerda, n+1) + quantidade(raiz.direita, n+1) + 1


# 2 - Escreva uma função para determinar a soma dos valores de todos os nós em uma árvore binária
def soma(raiz, n=0):
    if raiz is None:
        return 0
    return soma(raiz.esquerda, n+1) + soma(raiz.direita, n+1) + raiz.valor


# 3 - Escreva uma função para determinar a altura de uma árvore binária
def altura(raiz):
    if raiz is None:
        return 0
    else:
        if altura(raiz.esquerda) > altura(raiz.direita):    # verifica qual subarvore é maior
            m = altura(raiz.esquerda)
        else:
            m = altura(raiz.direita)
        return 1 + m


# 4 - Escreva uma função que calcula o maior valor em uma árvore binária
def maior(raiz):
    if raiz is None:
        return
    if raiz.direita is None:    # caminha na árvore a direita até que não haja mais nós. O último nó visitado é o maior
        return raiz.valor
    return maior(raiz.direita)


# 5 - Realizar uma busca por um determinado valor.
# Retornar True se encontrar
# Retornar False se não encontrar
def buscar(raiz, valor):
    if raiz is None:        # chegou na folha e não encontrou
        return False
    elif raiz.valor == valor:   # encontrou o valor em algum nó
        return True

    if valor < raiz.valor:      # verifica se elemento está à esquerda ou direita
        return buscar(raiz.esquerda, valor)
    else:
        return buscar(raiz.direita, valor)



# -----------------------------------------------------------------------------
print('-'*50)
print('TESTE 1:\nÁrvore com os valores: 5 7 4 1 9 6 3')

tree1 = Tree(5)
inserir(tree1, 7)
inserir(tree1, 4)
inserir(tree1, 1)
inserir(tree1, 9)
inserir(tree1, 6)
inserir(tree1, 3)

# imprimir(tree1)

print('\nResultado dos Testes:')

try:
    assert quantidade(tree1) == 7
    print('ACERTO - quantidade')
except AssertionError:
    print('ERRO   - quantidade')
except Exception:
    print('ERRO   - quantidade')

try:
    assert soma(tree1) == 35
    print('ACERTO - soma')
except AssertionError:
    print('ERRO   - soma')
except Exception:
    print('ERRO   - soma')

try:
    assert altura(tree1) == 4
    print('ACERTO - altura')
except AssertionError:
    print('ERRO   - altura')
except Exception:
    print('ERRO   - altura')

try:
    assert maior(tree1) == 9
    print('ACERTO - maior')
except AssertionError:
    print('ERRO   - maior')
except Exception:
    print('ERRO   - maior')

try:
    assert buscar(tree1, 5) is True
    assert buscar(tree1, 7) is True
    assert buscar(tree1, 4) is True
    assert buscar(tree1, 1) is True
    assert buscar(tree1, 9) is True
    assert buscar(tree1, 6) is True
    assert buscar(tree1, 3) is True
    print('ACERTO - buscar por valor existente')
except AssertionError:
    print('ERRO   - buscar por valor existente')
except Exception:
    print('ERRO   - buscar por valor existente')

try:
    assert buscar(tree1, 0) is False
    assert buscar(tree1, 2) is False
    assert buscar(tree1, 8) is False
    assert buscar(tree1, 10) is False
    assert buscar(tree1, 20) is False
    print('ACERTO - buscar por valor inexistente')
except AssertionError:
    print('ERRO   - buscar por valor inexistente')
except Exception:
    print('ERRO   - buscar por valor inexistente')


# -----------------------------------------------------------------------------
print('-'*50)
print('TESTE 2:\nÁrvore com os valores: 7 4 15 12 9 18 10 11 20 1 2')

tree2 = Tree(7)
inserir(tree2, 4)
inserir(tree2, 15)
inserir(tree2, 12)
inserir(tree2, 9)
inserir(tree2, 18)
inserir(tree2, 10)
inserir(tree2, 11)
inserir(tree2, 20)
inserir(tree2, 1)
inserir(tree2, 2)

# imprimir(tree2)

print('\nResultado dos Testes:')

try:
    assert quantidade(tree2) == 11
    print('ACERTO - quantidade')
except AssertionError:
    print('ERRO   - quantidade')
except Exception:
    print('ERRO   - quantidade')

try:
    assert soma(tree2) == 109
    print('ACERTO - soma')
except AssertionError:
    print('ERRO   - soma')
except Exception:
    print('ERRO   - soma')

try:
    assert altura(tree2) == 6
    print('ACERTO - altura')
except AssertionError:
    print('ERRO   - altura')
except Exception:
    print('ERRO   - altura')

try:
    assert maior(tree2) == 20
    print('ACERTO - maior')
except AssertionError:
    print('ERRO   - maior')
except Exception:
    print('ERRO   - maior')

try:
    assert buscar(tree2, 7) is True
    assert buscar(tree2, 4) is True
    assert buscar(tree2, 15) is True
    assert buscar(tree2, 12) is True
    assert buscar(tree2, 9) is True
    assert buscar(tree2, 18) is True
    assert buscar(tree2, 10) is True
    assert buscar(tree2, 11) is True
    assert buscar(tree2, 20) is True
    assert buscar(tree2, 1) is True
    assert buscar(tree2, 2) is True
    print('ACERTO - buscar por valor existente')
except AssertionError:
    print('ERRO   - buscar por valor existente')
except Exception:
    print('ERRO   - buscar por valor existente')

try:
    assert buscar(tree2, 0) is False
    assert buscar(tree2, 3) is False
    assert buscar(tree2, 5) is False
    assert buscar(tree2, 6) is False
    assert buscar(tree2, 8) is False
    assert buscar(tree2, 13) is False
    assert buscar(tree2, 14) is False
    assert buscar(tree2, 16) is False
    assert buscar(tree2, 17) is False
    assert buscar(tree2, 19) is False
    assert buscar(tree2, 25) is False
    print('ACERTO - buscar por valor inexistente')
except AssertionError:
    print('ERRO   - buscar por valor inexistente')
except Exception:
    print('ERRO   - buscar por valor inexistente')
