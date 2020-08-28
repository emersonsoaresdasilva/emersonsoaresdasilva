while True:
    letra = input()
    if letra == 'F':
        break
    for i in range(65, ord(letra) + 1):
        print(chr(i), end=' ')
    print()