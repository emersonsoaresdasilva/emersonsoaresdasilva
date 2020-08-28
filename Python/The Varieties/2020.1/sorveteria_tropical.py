Sabor = input()
Quantidade = int(input())

if Sabor.lower() == "morango" or Sabor.lower() == "cereja":
    Total = Quantidade*4.50
elif sabor.lower() == "damasco" or Sabor.lower() == "siriguela":
    Total = Quantidade*3.80
else:
    Total = Quantidade*2.75

print("%.2f"%Total)

if Quantidade > 2:
    print ("COM CALDA")
else:
    print("SEM CALDA")
