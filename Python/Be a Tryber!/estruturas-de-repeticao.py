#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 04 |
#   Estruturas de Repetição (Trybe)
#-------------------------------------

for i in range(10):#[0...9[
    print(i)

convidados = ['Elysson', 'Luana', 'Vinicius', 'Maria', 'Pedro', 'Priscila']

for convidado in convidados: #Para cada elemento da lista.
    print(convidado + ' está convidado.')

for i in range(len(convidados)):
    convidado = convidados[i]
    print(convidado + ' está convidado.')

saida = True
contador = 0

while contador > 5:
    contador += 1
    print('While contador: ' + str(contador))
