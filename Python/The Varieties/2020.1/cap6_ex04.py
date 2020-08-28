h = 1
denominador = 2
for numerador in range(3, 99+1, 4):
    h += numerador/denominador
    denominador += 2
print(h)
