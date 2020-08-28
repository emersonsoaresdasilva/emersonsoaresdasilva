p1 = 0 
p2 = 0
p3 = 0
n1 = float(input())
n2 = float(input())
n3 = float(input())

media = float(n1+n2+n3)/3

if n1 > media: p1 = 1 
if n2 > media: p2 = 1    
if n3 > media: p3 = 1
soma = p1+p2+p3
print(soma)
