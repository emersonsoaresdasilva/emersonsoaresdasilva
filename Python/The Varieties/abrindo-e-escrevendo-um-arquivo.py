#Para abrir um arquivo utilizamos a função open().
'''
f = open('nome_do_arquivo.txt', 'w')
'''
#Para escrever dados em um arquivo, utilizamos o métoodo write().
#Obs: Valores numéricos devem ser convertidos para string.
'''
f = open('nome_do_arquivo.txt', 'w')
f.write('Conteúdo do arquivo')
f.close() #Não podemos esquecer da operação de fechamento do arquivo, através do método close().
'''
'''
Se quisermos adicionar várias linhas ao arquivo,
devemos utilizar o caractere especial \n no fim de cada linha.
'''
# Se quisermos adicionar novas linhas a um arquivo já existente, usamos o modo de abertura a (de append).
f = open('nome_do_arquivo.txt', 'a')
print('Informe 3 nomes: ')
for _ in range(3):
    nome = input('Nome: ')
    f.write('%s\n' % (nome))
f.close()
