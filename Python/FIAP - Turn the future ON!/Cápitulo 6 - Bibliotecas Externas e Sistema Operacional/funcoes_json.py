import json
import os

def chamarMenu():
    opcao = int(input(
"""
<1> para registrar ativo.
<2> para exibir os ativos armazenados.

Digite a opção desejada: """))
    return opcao

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivo_json:
            dicionario = json.load(arquivo_json)
    else:
        dicionario = {}
    return dicionario

def gravar_arquivo(dicionario, arquivo):
    with open(arquivo, "w") as arquivo_json:
        json.dump(dicionario, arquivo_json)

def registrar(dicionario, arquivo):
    resposta = "S"
    while resposta == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        resposta = input("Digite <S> para continuar: ").upper()
        gravar_arquivo(dicionario, arquivo)
    return "O arquivo JSON foi gerado..."

def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data...........:", dado[0])
        print("Descrição......:", dado[1])
        print("Departamento...:", dado[2])

#Método dump().
'''
O método dump(), que pertence ao objeto “json”.
Esse método é formado, basicamente, por dois parâmetros:
o que será gravado, no nosso caso, o dicionário “inventario” e onde será gravado, quando definimos por meio do alias “arquivo_json”.
'''
#Método path.exists().
'''
“path.exists()”, retorna “True”, caso encontre o arquivo especificado como parâmetro ou "False" caso não encontrado.

Se o arquivo existir, então, preencha o dicionário com o conteúdo do arquivo, caso contrário (se o arquivo não existir), crie o dicionário “inventario” vazio.
'''
