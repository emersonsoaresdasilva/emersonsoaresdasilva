'''
Crie um programa que receba como entrada uma frase e uma palavra
e exiba a posição onde é encontrada a primeira ocorrência da palavra.
'''

frase = input('Frase: ')
palavra = input('Palavra: ')

qtd_ocorrencias = frase.count(palavra)

posicao = frase.index(palavra)
print('A posição é:',posicao)

for i in range(qtd_ocorrencias-1):
    posicao = frase[posicao+1:].index(palavra) + (posicao + 1)
    print('A posição é:',posicao)
