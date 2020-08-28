def mdc(x,y):
    a = max(x,y)
    b = min(x,y)
    if(a % b == 0):
        return b
    else:
        return mdc(b,(a%b))
    
x = int(input())
y = int(input())
print(mdc(x,y))
