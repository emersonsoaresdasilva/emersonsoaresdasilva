#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 02 |
#   Variáveis Built-Ins (Trybe)
#-------------------------------------

lista_convidados = ['Elysson', 'Priscila', 'Pedro', 'Maria']

print(lista_convidados) #Lista de convidados.

lista_convidados.append('Mauricio')

print(lista_convidados) #Inserindo +01 elemento na lista.

lista_convidados.remove('Elysson')

print(lista_convidados) #Removendo 01 elemento da lista.

print(lista_convidados[0]) #Pegando 01 elemento na lista.

print(lista_convidados[-1]) #Pegando o último elemento da lista.

lista_convidados.append(50)

print(lista_convidados)

#------------------------------------
#               Tupla
#------------------------------------

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1)

tupla3 = tupla1 + tupla2

print(tupla3)


#------------------------------------
#            Dicionário
#          Chave -> Valor!
#------------------------------------

dados_pessoais = {'nome': 'Batman', 'cidade': 'Gothan'}

print(dados_pessoais)

dados_pessoais['veiculo'] = 'Batmovel' #Inserindo +01 elemento no dicionário.

print(dados_pessoais)

del dados_pessoais['cidade'] #Removendo elemento no dicionário.

print(dados_pessoais)


