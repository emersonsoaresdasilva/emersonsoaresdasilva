def menor(a, b, c):
    m = a
    if b < m: m = b
    if c < m: m = c
    return m

def maior(a, b, c):
    m = a
    if b > m: m = b
    if c > m: m = c
    return m

def xereta():
    global x
    x = 90
    print('O que tem em x?', x)
    print('O que tem em y?', y)

x = maior(20,30,10)
y = menor(20,30,10)
print('maior:', x)
print('menor:', y)
xereta()


