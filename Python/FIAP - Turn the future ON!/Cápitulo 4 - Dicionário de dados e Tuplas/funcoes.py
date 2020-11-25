def perguntar():
    resposta = input(
        "O que deseja realizar?\n" +
        "<I> - Para Inserir um usuário\n" +
        "<P> - Para Pesquisar um usuário\n" +
        "<E> - Para Excluir um usuário\n" +
        "<L> - Para Listar um usuário\n" +
        "Digite a opção desejada: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                          input("Digite a última data de acesso: "),
                                          input("Qual a última estação acessada: ").upper()]

'''
    Na função pesquisar(), precisamos receber o dicionário (onde se pretende pesquisar) e a chave (o dado que será pesquisado).
    Logo após, vamos preencher uma lista com o resultado da pesquisa proveniente do uso da função get().
    Verificamos se a lista não está vazia (!= - representa diferente), caso esta condição seja verdadeira, vamos exibir os três dados que compõem a lista.
    Teremos, na primeira posição (zero), o nome do usuário; na segunda posição (um), a última data de acesso; e na terceira posição (dois), a última estação acessada.
    Caso não encontre a chave, não será retornada nenhuma mensagem;
'''


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome.............: " + lista[0])
        print("Último acesso....: " + lista[1])
        print("Última estacação.: " + lista[2])

'''
    Na função excluir(), também recebemos o dicionário de onde o objeto será excluído e a chave do objeto que se deseja excluir.
    Efetivamente, antes da exclusão, devemos verificar se a chave existe.
    Por isso, verificamos com a função get() se será retornado algo diferente de vazio e, se isso for verdade, invocamos o comando “del”, que eliminará o objeto de acordo com a chave que foi recebida.
'''

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Eliminado")

'''
    Na função listar(), precisaremos apenas do dicionário que contém os dados que desejamos exibir, com isso,
    montamos um foreach, mas perceba que, desta vez, utilizamos dois valores (chave e valor) para que possamos dar uma saída um pouco mais “clean” para o nosso usuário final.
    Poderíamos fazer de outras formas, inclusive, utilizando a nossa outra função pesquisar().
'''

def lista(dicionario):
    for chave, valor, in dicionario.items():
        print("Objeto.......")
        print("Login:", chave)
        print("Dados:", valor)
