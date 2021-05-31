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


# Percurso Pré-Ordem: imprime primeiro o conteúdo da raiz, em seguida imprime
# toda a subárvore esquerda e finalmente imprime toda a subárvore direita
def pre_ordem(raiz):
    if raiz is None:
        return
    print(raiz.valor, end=' ')
    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)


# Percurso Simétrico: imprime toda a subárvore esquerda, em seguida imprime o
# conteúdo da raiz e finalmente imprime toda a subárvore direita
def simetrica(raiz):
    if raiz is None:
        return
    simetrica(raiz.esquerda)
    print(raiz.valor, end=' ')
    simetrica(raiz.direita)


# Percurso Pós-Ordem: imprime toda a subárvore esquerda, em seguida imprime
# toda a subárvore direita e finalmente imprime o conteúdo da raiz
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
# Cada item é endentado quatro espaços por nível.
# A arvore é exibida "deitada", com a raiz à esquerda.
def imprimir(raiz, level=0):
    if raiz is None:
        return
    imprimir(raiz.direita, level+1)
    print('    '*level + str(raiz.valor))
    imprimir(raiz.esquerda, level+1)


# EXEMPLO DE PROGRAMA PRINCIPAL

# Cria a raiz da árvore (primeiro nó)
tree = Tree(49)

# Insere os demais nós
inserir(tree, 28)
inserir(tree, 83)
inserir(tree, 18)
inserir(tree, 40)
inserir(tree, 11)
inserir(tree, 19)
inserir(tree, 32)
inserir(tree, 44)
inserir(tree, 71)
inserir(tree, 97)
inserir(tree, 99)
inserir(tree, 95)
inserir(tree, 72)
inserir(tree, 69)

# Imprime a árvore
imprimir(tree)

# Imprime os percursos
print('\n\nPRÉ ORDEM:')
pre_ordem(tree)

print('\n\nSIMÉTRICA:')
simetrica(tree)

print('\n\nPÓS ORDEM:')
pos_ordem(tree)
