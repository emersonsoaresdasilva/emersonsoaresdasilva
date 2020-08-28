diaria = 30
dias = int(input())
km = int(input())
valor = (km*0.01) + (dias*diaria)
desconto = valor - (10*valor)/100
print('%.2F'%desconto)