def misterio(x,v,n):
    i = 0
    while i < n and v[i] != x:
        i += 1
    if i < n:
        return i
    else:
        return - 1
    return

a = ['b','x','d','v','e','r','e','p']

r1 = misterio('e',a,8)
r2 = misterio('z',a,8)
r3 = misterio('v',a,3)

print(r1,r2,r3)
    
#Resposta: 4 -1 -1
