def struct(Codigo,Nome,Credito):
    Codigo = Codigo
    Nome = Nome
    Credito = Credito
    print(Codigo)
    print(Nome)
    print('%.2F'%Credito)

Codigo = int(input())
Nome = input()
Credito = float(input())
struct(Codigo,Nome,Credito)