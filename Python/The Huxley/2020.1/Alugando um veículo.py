D = int(input())
K = int(input())

valor = D * 90

if (K>D*100):
        valor = valor + ((K-(D*100))*12)
print("%.2f" %valor)