n = str(input()).strip()

nome = n.split()

if len(nome) < 400:
    print(nome[len(nome)-1])
