def somar(V, N): #V: vetor númerico; N: tamanho do vetor
    Soma = 0
    I = 0
    while I < N:
        Soma += V[I]
        I += 1
    return Soma

Peso = [10, 20, 30]
X = somar(Peso, 3)
print('A soma é:',X)
    
