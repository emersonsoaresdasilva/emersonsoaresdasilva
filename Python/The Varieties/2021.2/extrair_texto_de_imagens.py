# Início →

# pip install easyocr

import easyocr

# Define Português como idioma:
reader = easyocr.Reader(['pt'])

# Lê a imagem:
resultados = reader.readtext('br116.jpg', paragraph=False)

# Itera sobre o resultado:
for resultado in resultados:
    print(f'Texto: {resultado[1]}\n')

# ← Fim