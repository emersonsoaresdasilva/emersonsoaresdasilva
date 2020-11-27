def chamarMenu():
    escolha = int(input(
"""
<1> para registrar ativo
<2> para persistir em arquivo
<3> para exibir ativos armazenados

Digite a opção desejada: """))
    return escolha

def registrar(dicionario):
    resposta = "S"
    while resposta == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resposta = input("Digite <S> para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" +
                      valor[0] + ";" +
                      valor[1] + ";" +
                      valor[2] + "\n")
    return "Persistido com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas
