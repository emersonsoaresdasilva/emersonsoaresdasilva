Litros = float(input())
Combustivel = input()

if(Combustivel=='A' or 'a'):
    print(Litros * 3.8997)
elif(Combustivel=='D' or 'd'):
    print(Litros * 3.6543)
else:
    print(Litros * 4.4009)
        
