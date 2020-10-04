#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 05 |
#     Formatando Strings (Trybe)
#-------------------------------------

'''
print('Minha idade é: ' + str(idade))
print('Minha idade é: {}'.format(idade)) #Convertendo internamente através do format.
print(f'Minha idade é: {idade}') #Formatação mais eficiente.
'''
nome = 'Emerson Soares da Silva'
idade = 19
dinheiro = 2.5
lista_itens = ['Garfo', 'Faca', 'Copo', 'Prato']

print(f'Meu nome é: {nome:.14} e eu tenho {idade:02} anos.') #Cortando os demais caracteres {nome:.10}.

print(f'Eu tenho R$ {dinheiro:.2f}')

print(f'Eu almoço com {lista_itens[0]} e {lista_itens[1]} no {lista_itens[-1]}')

print(f'Eu terei {idade + 30} anos daqui a 30 anos.')
