#Manipulação de Arquivos e JSON.

#Gerando um erro, pois não existe o arquivo especificado...
try:
    with open("teste.txt", "r") as arquivo:
        conteudo = arquivo.read()
        raise FileNotFoundError
except FileNotFoundError:
    print("Não existe o arquivo especificado.")
    
#Alterando o código.
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

#Sobrescrevendo o arquivo.
with open("teste.txt", "w") as arquivo:
    arquivo.write(
        "Continuação do texto...")
