import random

jogadas = ['pedra', 'papel', 'tesoura']

def jogar(ultima_jogada=None):
    if ultima_jogada is None:
        return random.choice(jogadas)
    indice = jogadas.index(ultima_jogada) + 1
    return jogadas[indice % len(jogadas)]

print(jogar())

'''
O comprimento da lista de jogadas é 3. Então, se for usado o operador "resto"
entre o índice e o comprimento da lista, teremos:

(0 % 3) é 0, e índice 0 é a posição do item Pedra na lista de jogadas.
(1 % 3) é 1, e índice 1 é a posição do item Papel na lista de jogadas.
(2 % 3) é 2, e índice 2 é a posição do item Tesoura na lista de jogadas.

(3 % 3) é 0, e índice 0 é a posição do item Pedra na lista de jogadas.
(4 % 3) é 1, e índice 1 é a posição do item Papel na lista de jogadas.
(5 % 3) é 2, e índice 2 é a posição do item Tesoura na lista de jogadas.

(6 % 3) é 0, e índice 0 é a posição do item Pedra na lista de jogadas.
(7 % 3) é 1, e índice 1 é a posição do item Papel na lista de jogadas.
(8 % 3) é 2, e índice 2 é a posição do item Tesoura na lista de jogadas.

E assim sucessivamente.
'''
