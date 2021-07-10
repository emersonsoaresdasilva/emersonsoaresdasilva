def funcao1(lista, item):
    for valor in lista:             # n
        if (valor == item):         # n
            return True             # 1
    return False                    # 1

def funcao2(lista, item):
    for i in range(len(lista)):     # n
        if (lista[i] == item):      # n
            return True             # 1
    return False                    # 1

def funcao3(lista, item):
    i = 0                           # 1
    while i < len(lista):           # n + 1
        if (lista[i] == item):      # n
            return True             # 1
        i += 1                      # n
    return False                    # 1

def funcao4(lista, item):
    n = False                       # 1
    for valor in lista:             # n
        if (valor == item):         # n
            n = True                # 1
    return n                        # 1
