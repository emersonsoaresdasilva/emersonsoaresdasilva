#Uma boa prática é sempre manipular arquivos utilizando o bloco with.
'''
Essa instrução fecha o arquivo automaticamente ao fim do bloco.
Caso uma exceção ocorra durante a manipulação do arquivo (especialmente durante a gravação dos dados),
é garantido que o arquivo será fechado.
'''
with open('meu_arquivo.txt', 'w') as f: #Apelidando para 'f'.
    f.write('Gravando alguns dados...\n')
    f.write('Esse é o exemplo da instrução with')

if f.closed: #Atributo closed: Testa se o arquivo está fechado.
    print('O arquivo está fechado.') #É garantido que o arquivo estará fechado após o block with.
else:
    print('O arquvo está aberto.')
