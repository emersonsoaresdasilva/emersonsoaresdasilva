# Criando pastas com Python:
import os

quantidade_pastas = int(input('Digite quantas pastas você quer criar: '))

for _ in range(quantidade_pastas):
    nome_pasta = input('Digite o nome da pasta: ')
    os.mkdir(nome_pasta)

# Criando pastas em lote:
nomes_pastas = ['Pasta 01', 'Pasta 02', 'Pasta 03']

for nome in nomes_pastas:
    os.mkdir(nome)
