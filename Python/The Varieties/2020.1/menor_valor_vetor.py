V = 10 * [0]
for i in range(10): #[0...10[
    V[i] = int(input('Valor: '))

Menor = V[0]
for i in range(1, 10): #[1...10[
    if V[i] < Menor:
        Menor = V[i]
print('O menor valor é: ',Menor)
