f = open('criando-um-arquivo-csv.csv', 'r') #Qual arquivo você vai ler? 'nome-do-arquivo.csv'
pessoas = []

for linha in f:
    linha = linha.rstrip()
    pessoa = linha.split(';')
    #Como o arquivo texto só armazena strings, é necessário converter os dados para o tipo original.
    pessoa[1] = int(pessoa[1])      #Converte o ano para inteiro.
    pessoa[2] = float(pessoa[2])    #Converte a altura para float.
    pessoas.append(pessoa)
    print(linha)                    #Exibindo os dados (teste).
f.close()

