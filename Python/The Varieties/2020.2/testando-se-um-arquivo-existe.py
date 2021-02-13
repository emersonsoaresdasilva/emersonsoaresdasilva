#É possível testar se um arquivo existe através da função exists() do módulo os.path

from os.path import exists

nome_arquivo = 'nome_do_arquivo.txt'

if exists(nome_arquivo):
    print('O arquivo existe! Segue o conteúdo:')
    f = open('nome_do_arquivo.txt', 'r') #Agora sim podemos abrir o arquivo sem problemas...
    print(f.read())
    f.close()
else:
    print('Não for possível localizar o arquivo.')
