Ano = int(input())
if (Ano%4==0 and Ano%100!=0) or (Ano%400==0):
    print("Bissexto")
else:
    print("Nao bissexto")