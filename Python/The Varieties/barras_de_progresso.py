# Início →

# pip install tqdm

from tqdm import tqdm

if __name__ == '__main__':
    numeros = range(int(10e7))
    for _ in tqdm(numeros, colour='blue', desc='Processando'):
        pass
# ← Fim