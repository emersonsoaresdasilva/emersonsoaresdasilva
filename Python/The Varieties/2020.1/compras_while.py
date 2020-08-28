'''
Crie um programa que recebe como entrada a quantidade de produtos que um consu-
midor comprou em um shopping. O programa deverá solicitar o valor de cada,
produto, somar os valores e exibir o total da compra.
'''

Quantidade = int(input('Quantidade de produtos: '))
Soma = 0
Contador = 0

while Contador < Quantidade:
    Valor_produto = float(input('Valor do produto: '))
    Soma += Valor_produto
    Contador += 1
print('O total da compra é: R$ %.2F'%Soma)
