'''
Crie um programa que receba como entrada a nota das ACs de um aluno e, ao final,
exiba a nota mínima que ele deverá conseguir na prova para ser aprovado.
desktop.ini
Restríções: funções/métodos permitidos: sum, min, max, range e print.
'''

def preenche(v, n):
    for i in range(n):
        v[i] = float(input('Vetor[%d]: '% i))

def media_acs(acs, n):
    return (sum(acs) - min(acs)) / 4

acs = 5 * [0.0]
preenche(acs, 5)
mac = media_acs(acs, 5)
prova = (6 - 0.5*mac) / 0.5
print(prova)

'''
nf = 0.5*mac + 0.5*prova
nf >= 6
0.5*mac + 0.5*prova >= 6
0.5*prova >= 6 - 0.5*mac
prova >= (6 - 0.5*mac) / 0.5
'''
