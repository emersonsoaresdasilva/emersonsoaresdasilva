def converter(codigo):
    for indice in range(len(codigo)):
        codigo[indice] = int(codigo[indice])
    return codigo

def traduzir(codigo):
    codigo = converter(codigo)
    frase = ''
    for indice in range(len(codigo)):
        letra = codigo[indice]
        if letra != 0:
            frase += chr(codigo[indice] + 96)
        else:
            frase += ' '
    return frase

codigo = input().split()
frase = traduzir(codigo)

while frase != 'fim':
    print(frase)
    codigo = input().split()
    frase = traduzir(codigo)