'''
Uma outra situação em que podemos utilizar as tuplas é quando usarmos a função “enumerate()” em uma lista.

Mas quando precisaremos utilizar a função “enumerate()” em uma lista?

Quando quisermos numerar cada componente da lista a fim de garantir que cada elemento dela poderá ser utilizado como dado chave de um dicionário.
'''
usuarios = {}
resposta = "S"
emails = []

while resposta == "S":
    emails.append(input("Digite um e-mail: ").lower())
    resposta = input("Digite <S> para continuar: ").upper()

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("Email:", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]

for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])
