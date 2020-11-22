#Criando nossas variáveis.
"""
nome = 'Emerson Soares da Silva'
empresa = 'Centro Universitário Sumaré.'
quantidade_de_funcionarios = 150
mediaMensalidade = 750.00
print(nome + ' trabalha na empresa ' + empresa)
print('Possui:', quantidade_de_funcionarios, 'funcionários.')
print(f'A média da mensalidade é de: {mediaMensalidade:.2f}')
"""

#Criando variáveis | input.
nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))
print()
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print(f"A média da mensalidade é de: {mediaMensalidade:.2f}\n")
print("==============| Verifique os tipos de dados abaixo |==============\n")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))
print()
print("==============| Fim da verificação tipos de dados |==============\n")

responsavel = input("Digite o nome do responsável: ")
funcionario = input("Digite o nome do funcionário: ")
evento = input("Digite o nome do evento: ")
valor = float(input("Digite o valor que será ressarcido: "))
print(f"Declaro para o senhor {responsavel} que o senhor {funcionario} esteve presente no evento {evento} e gastou o valor de R$ {valor:.2f} com a entrada.")
