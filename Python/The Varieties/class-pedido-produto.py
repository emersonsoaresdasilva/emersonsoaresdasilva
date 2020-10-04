#Definição da classe produto.
class Produto:

    def __init__(self, nome, preco, quantidade):

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

#Definição da classe pedido.
class Pedido:

    def __init__(self):        
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        soma_total = 0.0
        for i in range(0, len(self.produtos)): # ou seja, i varia de 0 até len(self.produtos)-1

            #soma_total = soma_total + (self.produtos[i].preco * self.produtos[i].quantidade)
            produto = self.produtos[i]
            soma_total += (produto.preco * produto.quantidade)

        return soma_total       
     
#Programa Principal

cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor()) # imprime 20.90
