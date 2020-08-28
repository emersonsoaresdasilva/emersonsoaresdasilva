def contar_dig_pares(n):
    
    cont = 0
    for x in n:
        if int(x)%2==0:
            cont +=1
    print(cont)

n = input()
contar_dig_pares(n)
