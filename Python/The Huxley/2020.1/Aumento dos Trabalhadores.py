salario = float(input())

if salario > 500.00:
    aumento = salario * 1.10
    print('%.2F'%aumento)
elif salario > 300.00 < 500.00:
    aumento = salario * 1.07
    print('%.2F'%aumento)
else:
    aumento = salario * 1.05
    print('%.2F'%aumento)