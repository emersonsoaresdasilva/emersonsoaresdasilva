'''
pH = int(input('Digite o pH da solucao:'))
print()

if(pH >= 0 and pH <=14):
    if(pH > 7 <= 14):
        print('Essa solucao e basica.')
    elif(pH < 7 >= 0):
        print('Essa solucao e acida.')
    else:
        print('Essa solucao e neutra.')
else:
    print('Valor deve estar entre 0 e 14.')

'''
'''
pH = float(input('Digite o pH da solucao:'))

if(pH >= 0.0 and pH <= 14.0):
    if(pH > 7.0 <= 14.0):
        print('Solucao basica')
    elif(pH < 7.0 >= 0.0):
        print('Solucao acida')
    else:
        print('Solucao neutra')
else:
    print('Valor do pH deve estar entre 0 e 14')
'''
pH = float(input())

if(pH >= 1.0 and pH <= 14.0):
    if(pH > 7.0 <= 14.0):
        print('Basica')
    elif(pH < 7.0 >= 1.0):
        print('Acida')
    else:
        print('Neutra')
