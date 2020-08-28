aux  = int
a = int (input())
b = int (input())
c = int (input())

if (a>b):
    aux=a
    a=b
    b=aux
if (b>c):
    aux=b
    b=c
    c=aux
if (a>b):
    aux=a
    a=b
    b=aux

print(a)
print(b)
print(c)