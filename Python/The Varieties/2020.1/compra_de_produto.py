Compra = float(input("Valor da compra: "))

if(Compra<20.0):
    Venda = Compra * 1.45
    print(Venda)
else:
    Venda = Compra * 1.30
    print(Venda)
