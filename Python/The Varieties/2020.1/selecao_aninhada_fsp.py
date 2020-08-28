def emprestimo():
    sb    = float(input())  # salário bruto (reais)
    tempo = int(input())    # tempo (anos)
    emp   = float(input())  # empréstimo (reais)

    if sb > 2000.00:
        if tempo > 2:
            juros = emp * 0.15
        else:
            juros = emp * 0.20
        print(emp + juros)
    else:
        print('Empréstimo negado')
    return

# PROGRAMA PRINCIPAL

emprestimo()
