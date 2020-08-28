def emprestimo(sb, tempo, emp):
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

a = float(input())  # salário bruto (reais)
b = int(input())    # tempo (anos)
c = float(input())  # empréstimo (reais)

emprestimo(a, b, c)
