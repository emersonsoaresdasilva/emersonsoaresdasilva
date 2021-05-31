# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS DO GRUPO (máximo 6)
# Emerson Soares da Silva
# Igor de Souza Teixeira
# ALUNO 3
# ALUNO 4
# ALUNO 5
# ALUNO 6

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
# Cada item é Indentado quatro espaços por nível.
# A arvore é exibida "deitada", com a raiz à esquerda.
def imprimir(raiz, level=0):
    if raiz is None:
        return
    imprimir(raiz.direita, level+1)
    print('    '*level + str(raiz.valor))
    imprimir(raiz.esquerda, level+1)

# ATIVIDADE: Implementar os métodos abaixo

# 1 - Retornar a quantidade de nós de uma árvore
def quantidade(raiz):
    if raiz is None:
        return 0
    return 1 + quantidade(raiz.esquerda) + quantidade(raiz.direita)

# 2 - Retornar a soma dos valores de todos os nós de uma árvore
def soma(raiz):
    if raiz is None:
        return 0
    return raiz.valor + soma(raiz.esquerda) + soma(raiz.direita)
    
# 3 - Retornar a altura de uma árvore
def altura(raiz):
    if raiz is None:
        return False
    else:
        altura_esquerda = altura(raiz.esquerda)
        altura_direita = altura(raiz.direita)
        if altura_direita > altura_esquerda:
            return altura_direita + 1
        else:
            return altura_esquerda + 1  

# 4 - Retornar o maior valor de uma árvore
def maior(raiz):
    raiz_atual = raiz # Guardei a raiz atual.
    while raiz_atual.direita: # Enquanto tiver filho na raiz.
        raiz_atual = raiz_atual.direita # A raiz atual recebe o filho.
    return raiz_atual.valor # Retorna o valor do maior filho.

# 5 - Realizar uma busca por um determinado valor.
# Retornar True se encontrar
# Retornar False se não encontrar
def buscar(raiz, valor):
    if raiz is None:
        return False
    elif raiz.valor is valor:
        return True
    elif valor < raiz.valor:
        return buscar(raiz.esquerda, valor)
    else:
        return buscar(raiz.direita, valor)

# EXEMPLO DE PROGRAMA PRINCIPAL

# Árvore com a inserção dos nós: 42, 16, 57, 8, 35, 48, 11, 5
tree = Tree(42)
inserir(tree, 16)
inserir(tree, 57)
inserir(tree, 8)
inserir(tree, 35)
inserir(tree, 48)
inserir(tree, 11)
inserir(tree, 5)
imprimir(tree)

print("\n")
print("Quantidade de nós:", quantidade(tree))

print("Somatório dos nós:", soma(tree))

print("Altura da árvore:", altura(tree))

print("Maior nó da árvore:", maior(tree))

print("Buscar um valor:", buscar(tree, 5))