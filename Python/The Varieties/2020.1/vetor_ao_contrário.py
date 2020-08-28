'''
O programa a seguir deverá preencher completamente o vetor criado com números
inteiros dados pelo usuário e, ao final, exibir os itens do vetor na sequência
contrária à que foi preenchido.
Assinale a alternativa que contém os valores que substituem adequadamente
os símbolos ? (interrogação), e na ordem correta,
de modo que o programa funcione conforme solicitado.
'''
#----------------------------------
#      VETORES AO CONTRÁRIO
#----------------------------------
n = int(input("Tamanho do vetor: "))
v = n * [0]

inicio = 0
fim = n
passo = -1

for i in range(inicio,fim):
    v[i] = int(input('valor: '))

for i in range(fim - 1, inicio - 1, passo):
    print(v[i], end=' ')

#Nenhuma das outras alternativas.
