'''
Na primeira linha um inteiro representando o código do cliente;
na linha seguinte uma string sem espaços representando o nome do cliente;
na linha seguinte um valor real indicando o valor do crédito que o cliente possui.
'''

def struct(Codigo,Nome,Credito):
    Codigo = Codigo
    Nome = Nome
    Credito = Credito
    return Codigo, Nome, '%.2F'%Credito

Codigo = int(input())
Nome = input()
Credito = float(input())
print(struct(Codigo,Nome,Credito))
