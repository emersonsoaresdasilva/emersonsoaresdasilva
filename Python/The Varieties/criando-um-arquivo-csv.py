#Podemos usar o formato csv (comma-separated values) para organizar registros em uma linha.
f = open('criando-um-arquivo-csv.csv', 'w')
nome = input('Informe o nome: ')

while nome != '': #Encerra ao ler um nome vazio.
    ano = int(input('Informe o ano de nascimento: '))
    altura = float(input('Informe a altura: '))
    f.write('%s;%d;%.2f\n' % (nome, ano, altura)) #Observe o formato dos dados.
    print('-'*30)
    nome = input('Informe o nome: ')
f.close()
    
