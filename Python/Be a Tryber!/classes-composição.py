#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 08 |
#        Composição (Trybe)
#-------------------------------------

class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoCompras:
    def __init__(self, cliente, produtos):
        self.numero_pedido = '123'
        self.produtos = produtos
        self.cliente = cliente

    @property #Chamando como atributo.
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco

        return total

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f'Fechando o pedido: {self.numero_pedido}')
        print(f'Valor do carrinho: {self.valor_carrinho}')
        print(f'Nome do cliente: {self.cliente.nome}')
        print('Obrigado pela compra!')

cliente = Cliente('Emerson', '123456')
televisao = Produto('Televisão', 1000.90)
maquina_cafe = Produto('Maquina de Café', 89.80)

produtos = [televisao, maquina_cafe]

carrinho = CarrinhoCompras(cliente, produtos)

teclado = Produto('Teclado Mecânico', 175.20)
carrinho.adicionar_produto(teclado)

carrinho.remover_produto(televisao)

print(carrinho.valor_carrinho) #Verificando o status atual.
print(carrinho.fechar_carrinho()) #Verificando o fechamento do carrinho.
