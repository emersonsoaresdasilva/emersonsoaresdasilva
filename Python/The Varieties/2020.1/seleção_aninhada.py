#Versão do Programa Principal!

SB = float(input()) #Salário Bruto (Reais)
TEMPO = int(input()) #Tempo de Cliente (Anos)
EMP = float(input()) #Empréstimo (Reais)

if SB > 2000.00:
    if TEMPO > 2:
        juros = EMP * 0.15
    else:
        juros = EMP * 0.20
    print(EMP + juros)
else:
    print("Empréstimo negado")

#Versão função sem parâmetro!
'''
def emprestimo():
    SB = float(input()) #Salário Bruto (Reais)
    TEMPO = int(input()) #Tempo de Cliente (Anos)
    EMP = float(input()) #Empréstimo (Reais)

    if SB > 2000.00:
        if TEMPO > 2:
            juros = EMP * 0.15
        else:
            juros = EMP * 0.20
        print(EMP + juros)
    else:
        print("Empréstimo negado")
    return
'''

#Versão função com parâmetro!
'''
SB = float(input()) #Salário Bruto (Reais)
TEMPO = int(input()) #Tempo de Cliente (Anos)
EMP = float(input()) #Empréstimo (Reais)

emprestimo(SB, TEMPO, EMP)

def emprestimo(SB, TEMPO, EMP):
    if SB > 2000.00:
        if TEMPO > 2:
            juros = EMP * 0.15
        else:
            juros = EMP * 0.20
        print(EMP + juros)
    else:
        print("Empréstimo negado")
    return
'''
