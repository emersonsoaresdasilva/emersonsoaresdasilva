def inverter_string(palavra):
    palavra = palavra[::-1]
    return palavra

palavra = input()
if len(palavra) < 255: print(inverter_string(palavra))

