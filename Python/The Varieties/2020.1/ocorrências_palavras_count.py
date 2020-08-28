'''
Crie um programa que receba como entrada uma frase e uma palavra e exiba a quantidade de vezes que
a palavra ocorre na frase.
'''

frase = input('Frase: ')
palavra = input('Palavra: ')
qtd = frase.count(palavra)
print('Ocorrências:',qtd)
