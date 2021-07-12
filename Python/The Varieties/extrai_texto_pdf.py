# Início →

# pip install pymupdf

import fitz

# Abra o arquivo em PDF.
with fitz.open('nome_arquivo.pdf') as arquivo_pdf:
    texto = ""

    for pagina in arquivo_pdf:
        texto += pagina.getText()
print(texto)

# ← Fim