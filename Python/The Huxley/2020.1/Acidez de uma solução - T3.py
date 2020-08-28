pH = float(input('Digite o pH da solucao:'))
print()

if(pH >= 0.0 and pH <= 14.0):
    if(pH > 7.0 <= 14.0):
        print('Solucao basica')
    elif(pH < 7.0 >= 0.0):
        print('Solucao acida')
    else:
        print('Solucao neutra')
else:
    print('Valor do pH deve estar entre 0 e 14')