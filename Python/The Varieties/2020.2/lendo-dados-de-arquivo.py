f = open('nome_do_arquivo.txt', 'r')

print('Nomes contidos no arquivo:')
for linha in f:
    print(linha.rstrip())
f.close()

#Outros métodos  úteis:
'''
readline(): lê uma linha por vez.
readlines(): lê todas as linhas e devolve o resultado como o tipo lista.
read(): lê todo o conte ́udo do arquivo de uma só vez.
'''
