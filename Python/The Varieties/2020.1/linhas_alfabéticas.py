while True:
    letra = input()
    if letra == 'F':
        break
    for i in range(65, ord(letra) + 1):
        print(chr(i), end=' ')
    print()

'''
def ler_letra():
    while True:
        letra = input()
        if len(letra) == 1 and 'A' <= letra <= 'Z':
            return letra
        else: print('Digite uma letra de A a Z')
'''
