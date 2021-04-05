import string
from random import choice

def gerar_senhas(tamanho):
    return ''.join([choice(string.ascii_lowercase + string.digits + '@#') for i in range(tamanho)])

# Quantos caracteres a senha terá e quantas eu quero.
tamanho, quantidade = 7, 1000

for _ in range(quantidade):
    print(gerar_senhas(tamanho))