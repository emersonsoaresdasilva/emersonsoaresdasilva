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
