#Começando nossa ferramenta...
'''
usuarios = {}
opcao = input(
    "O que deseja realizar?\n" +
    "<I> - Para Inserir um usuário\n" +
    "<P> - Para Pesquisar um usuário\n" +
    "<E> - Para Excluir um usuário\n" +
    "<L> - Para Listar um usuário\n" +
    "Digite a opção desejada: ").upper()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        usuarios[
            input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
            input("Digite a última data de acesso: "),
            input("Qual a última estação acessada: ").upper()
        ]        
    opcao = input(
        "O que deseja realizar?\n" +
        "<I> - Para Inserir um usuário\n" +
        "<P> - Para Pesquisar um usuário\n" +
        "<E> - Para Excluir um usuário\n" +
        "<L> - Para Listar um usuário\n" +
        "Digite a opção desejada: ").upper()
'''
#Devemos utilizar “F-U-N-Ç-Õ-E-S” (Aprimorando o código).
'''
Olhando para o nosso código, podemos dividi-lo em duas ações: preencher a variável “opcao” e preencher o dicionário de dados.
'''

from funcoes import *

usuarios={}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()
