class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Lista:
    def __init__(self):
        self.cabeca = None

    def insere_no_inicio(self, dado):
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(dado)

        if self.cabeca is None:                     # lista vazia
            # define o novo nodo como cabeça da lista
            self.cabeca = novo_nodo
        else:                                      # lista não vazia
            # novo nodo aponta para a cabeça da lista.
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo

    def insere_no_final(self, dado):
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(dado)

        if self.cabeca is None:                     # lista vazia
            # define o novo nodo como cabeça da lista
            self.cabeca = novo_nodo
        else:                                       # lista não vazia
            nodo_atual = self.cabeca
            while nodo_atual.proximo is not None:
                nodo_atual = nodo_atual.proximo
            nodo_atual.proximo = novo_nodo

    def remove_do_inicio(self):
        if self.cabeca is None:                     # lista vazia
            raise 'Fila Vazia'
        else:                                       # lista não vazia
            # altera a cabeça da lista
            self.cabeca = self.cabeca.proximo

    def remove_do_final(self):
        if self.cabeca is None:                     # lista vazia
            raise 'Fila Vazia'
        elif self.cabeca.proximo is None:           # apenas 1 item
            self.cabeca = None
        else:                                       # lista não vazia
            nodo_atual = self.cabeca
            nodo_anterior = None

            # percorre os nós até o penultimo item
            while nodo_atual.proximo is not None:
                nodo_anterior = nodo_atual          # atualiza o nó anterior
                nodo_atual = nodo_atual.proximo     # atualiza o nó atual

            nodo_anterior.proximo = None            # remove ultimo item

    def buscar(self, valor):
        nodo_atual = self.cabeca
        while nodo_atual is not None:           # percorre os nós da lista
            if nodo_atual.dado == valor:        # verifica se encontrou o item
                return True
            nodo_atual = nodo_atual.proximo     # atualiza o nó atual
        return False                        # terminou a lista e não encontrou

    def imprimir(self):
        nodo_atual = self.cabeca
        lista = ""
        while nodo_atual is not None:           # percorre os nós da lista
            lista += str(nodo_atual.dado) + ", "
            # atualiza o nó atual
            nodo_atual = nodo_atual.proximo
        return lista[0:len(lista)-2]

    """
    EXERCICIO 1:
    Implemente o método 'tamanho' que retorna a quantidade de itens da lista.
    Caso a lista esteja vazia, deve retornar zero.
    """
    def tamanho(self):
        nodo_atual = self.cabeca
        tamanho = 0
        while nodo_atual is not None:
            tamanho += 1
            nodo_atual = nodo_atual.proximo
        return tamanho
    """
    EXERCICIO 2:
    implemente o método 'menor' que retorna o menor item contido na lista.
    Caso a lista esteja vazia deve retornar None.
    """
    def menor(self):
        if self.cabeca is None:
            return None
        menor = self.cabeca.dado
        nodo_atual = self.cabeca.proximo
        while nodo_atual is not None:
            if nodo_atual.dado < menor:
                menor = nodo_atual.dado
            nodo_atual = nodo_atual.proximo
        return menor
    """
    EXERCICIO 3:
    Implemente o método 'soma' que retorna o somatório dos itens da lista.
    Caso a lista esteja vazia, deve retornar None.
    """
    def soma(self):
        if self.cabeca is None:
            return None
        nodo_proximo = self.cabeca.proximo
        soma = self.cabeca.dado
        while nodo_proximo is not None:
            soma += nodo_proximo.dado
            nodo_proximo = nodo_proximo.proximo
        return soma
    """
    EXERCICIO 4:
    Implemente o método 'media' que retorna a media dos itens da lista.
    Caso a lista esteja vazia, deve retornar None.
    """
    def media(self):
        return None if self.cabeca is None else self.soma() / self.tamanho()
    """
    EXERCICIO 5:
    Implemente o método 'substituir' que recebe como entrada dois itens,
    e substitui todas as ocorrências do item 'velho' pelo item 'novo'.
    """
    def substituir(self, velho, novo):
        nodo_atual = self.cabeca
        while nodo_atual is not None:
            if nodo_atual.dado == velho:
                nodo_atual.dado = novo
            nodo_atual = nodo_atual.proximo

# # Exemplo de utilização da classe Lista
# lista = Lista()
# lista.insere_no_inicio(10)
# lista.insere_no_inicio(20)
# lista.insere_no_inicio(30)
# lista.insere_no_inicio(40)
# print(lista.imprimir())         # 40, 30, 20, 10

# lista.insere_no_final(50)
# lista.insere_no_final(60)
# lista.insere_no_final(70)
# lista.insere_no_final(80)
# print(lista.imprimir())         # 40, 30, 20, 10, 50, 60, 70, 80

# print(lista.buscar(10))         # True
# print(lista.buscar(100))        # False

# lista.remove_do_inicio()
# lista.remove_do_inicio()
# print(lista.imprimir())         # 20, 10, 50, 60, 70, 80

# lista.remove_do_final()
# lista.remove_do_final()
# print(lista.imprimir())         # 20, 10, 50, 60

# Testes para os métodos a serem implementados
print("\nEXECUÇÃO DOS TESTES:\n")


def test_01_tamanho():
    # tamnho de lista vazia
    try:
        lista3 = Lista()
        assert lista3.tamanho() == 0, 'Tamanho deve ser zero'
        print("ACERTO test_01_tamanho")
    except AssertionError as erro:
        print("ERRO test_01_tamanho: ", erro)


def test_02_tamanho():
    # tamanho de lista com 1 item
    try:
        lista = Lista()
        lista.insere_no_final(10)
        assert lista.tamanho() == 1, 'Tamanho deve ser 1'
        print("ACERTO test_02_tamanho")
    except AssertionError as erro:
        print("ERRO test_02_tamanho: ", erro)


def test_03_tamanho():
    # tamanho de lista com vários itens
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(50)
        assert lista.tamanho() == 5, 'Tamanho deve ser 5'
        print("ACERTO test_03_tamanho")
    except AssertionError as erro:
        print("ERRO test_03_tamanho: ", erro)


def test_04_menor():
    # menor item em lista vazia
    try:
        lista = Lista()
        assert lista.menor() is None, 'Menor item deve ser None'
        print("ACERTO test_04_menor")
    except AssertionError as erro:
        print("ERRO test_04_menor: ", erro)


def test_05_menor():
    # menor item em lista com 1 item
    try:
        lista = Lista()
        lista.insere_no_final(10)
        assert lista.menor() == 10, 'Menor item deve ser 10'
        print("ACERTO test_05_menor")
    except AssertionError as erro:
        print("ERRO test_05_menor: ", erro)


def test_06_menor():
    # menor item em lista com varios itens
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(5)
        lista.insere_no_final(30)
        lista.insere_no_final(5)
        assert lista.menor() == 5, 'Menor item deve ser 5'
        print("ACERTO test_06_menor")
    except AssertionError as erro:
        print("ERRO test_06_menor: ", erro)


def test_07_menor():
    # menor item em lista com varios itens
    try:
        lista = Lista()
        lista.insere_no_final(30)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(7)
        assert lista.menor() == 7, 'Menor item deve ser 7'
        print("ACERTO test_07_menor")
    except AssertionError as erro:
        print("ERRO test_07_menor: ", erro)


def test_08_soma():
    # soma de lista vazia
    try:
        lista = Lista()
        assert lista.soma() is None, 'Somatório de lista vazia deve ser None'
        print("ACERTO test_08_soma")
    except AssertionError as erro:
        print("ERRO test_08_soma: ", erro)


def test_09_soma():
    # soma de lista com 1 item
    try:
        lista = Lista()
        lista.insere_no_final(10)
        assert lista.soma() == 10, 'Somatório da lista deve ser 10'
        print("ACERTO test_09_soma")
    except AssertionError as erro:
        print("ERRO test_09_soma: ", erro)


def test_10_soma():
    # soma de lista com vários itens
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(35)
        assert lista.soma() == 65, 'Somatório da lista deve ser 65'
        lista.insere_no_final(60)
        lista.insere_no_final(100)
        assert lista.soma() == 225, 'Somatório da lista deve ser 225'
        print("ACERTO test_10_soma")
    except AssertionError as erro:
        print("ERRO test_10_soma: ", erro)


def test_11_media():
    # media de lista vazia
    try:
        lista = Lista()
        assert lista.media() is None, 'Média de lista vazia deve ser None'
        print("ACERTO test_11_media")
    except AssertionError as erro:
        print("ERRO test_11_media: ", erro)


def test_12_media():
    # media de lista com 1 item
    try:
        lista = Lista()
        lista.insere_no_final(10)
        assert lista.media() == 10, 'Média da lista deve ser 10'
        print("ACERTO test_12_media")
    except AssertionError as erro:
        print("ERRO test_12_media: ", erro)


def test_13_media():
    # media de lista com vários itens
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        assert lista.media() == 25, 'Média da lista deve ser 25'
        lista.insere_no_final(50)
        lista.insere_no_final(60)
        assert lista.media() == 35, 'Média da lista deve ser 35'
        print("ACERTO test_13_media")
    except AssertionError as erro:
        print("ERRO test_13_media: ", erro)


def test_14_substituir():
    # substituir item em lista vazia
    try:
        lista = Lista()
        lista.substituir(100, 200)
        assert lista.imprimir() == '', 'lista deve ser vazia'
        print("ACERTO test_14_substituir")
    except AssertionError as erro:
        print("ERRO test_14_substituir: ", erro)


def test_15_substituir():
    # substituir item em lista (item inexistente)
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.substituir(100, 200)
        assert lista.imprimir() == '10, 20, 30, 40', 'lista deve ser: 10, 20, 30, 40'
        print("ACERTO test_15_substituir")
    except AssertionError as erro:
        print("ERRO test_15_substituir: ", erro)


def test_16_substituir():
    # substituir item em lista
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.substituir(20, 200)
        assert lista.imprimir() == '10, 200, 30, 40', 'lista deve ser: 10, 200, 30, 40'
        print("ACERTO test_16_substituir")
    except AssertionError as erro:
        print("ERRO test_16_substituir: ", erro)


def test_17_substituir():
    # substituir item em lista
    try:
        lista = Lista()
        lista.insere_no_final(20)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(20)
        lista.substituir(20, 100)
        assert lista.imprimir() == '100, 100, 30, 100', 'lista deve ser: 100, 100, 30, 100'
        print("ACERTO test_17_substituir")
    except AssertionError as erro:
        print("ERRO test_17_substituir: ", erro)


test_01_tamanho()
test_02_tamanho()
test_03_tamanho()
test_04_menor()
test_05_menor()
test_06_menor()
test_07_menor()
test_08_soma()
test_09_soma()
test_10_soma()
test_11_media()
test_12_media()
test_13_media()
test_14_substituir()
test_15_substituir()
test_16_substituir()
test_17_substituir()
