Valor_divida = int(input())
Valor_mensal = int(input())

while(Valor_divida > 0):
    print('(antes)',Valor_divida)
    if Valor_divida > Valor_mensal:
        Valor_divida -= Valor_mensal
    else:
        Valor_divida = 0
    print('(depois)',Valor_divida)