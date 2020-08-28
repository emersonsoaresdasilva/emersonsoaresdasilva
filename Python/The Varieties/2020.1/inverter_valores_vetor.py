'''
Crie uma função que receba como parâmetro um vetor V e o seu tamanho N.
A função deverá criar um vetor auxiliar com os itens de V em sequência
contrária.
A função deverá retornar auxiliar.
'''

def inverter_valores_vetor(v,n):
    lista = n * [0]
    j = n - 1
    for i in range(n):
        lista[j] = v[i]
        j -= 1
    return lista

v = 3 * [0]
for i in range(3):
    v[i] = int(input('Valor: '))

lista = inverter_valores_vetor(v, 3)

for i in range(3):
    print(lista[i], end=' ')
