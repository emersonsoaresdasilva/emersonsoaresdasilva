pH = float(input())

if(pH >= 1.0 and pH <= 14.0):
    if(pH > 7.0 <= 14.0):
        print('Basica')
    elif(pH < 7.0 >= 1.0):
        print('Acida')
    else:
        print('Neutra')