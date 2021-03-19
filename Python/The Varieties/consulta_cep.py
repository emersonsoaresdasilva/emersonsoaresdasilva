import requests
from flask import Flask

# Brincando com python... :)

# Usa a biblioteca requests para abrir uma conexao com o viacep.
def search(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code != 200:
        return ValueError
    dicionario_retornado = response.json()
    return dicionario_retornado

def cep_to_bairro(cep):
    dicionario_retornado = search(cep)
    if dicionario_retornado != ValueError:       
        return dicionario_retornado['bairro']
    return dicionario_retornado

def cep_to_logradouro(cep):
    dicionario_retornado = search(cep)
    if dicionario_retornado != ValueError:       
        return dicionario_retornado['logradouro']
    return dicionario_retornado

# Gerar um objeto chamado app, uma burocracia que a gente faz sempre.
app = Flask(__name__)

# --> --> --> --> --> --> --> --> --> --> -->
#               • Bairro / Rua •
#
# O meu servidor tem uma URL bairro/cep
# Eu (Browser) --> meu servidor --> viacep
#
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

@app.route("/bairro/<cep>")
def bairro(cep):
    bairro = cep_to_bairro(cep)
    if bairro != ValueError:
        return {'bairro': bairro}
    return {
        'erro':     f'O CEP informado esta incorreto.',
        'codigo':   f'{500}',
        'cep':      f'{cep}'
        }

@app.route("/logradouro/<cep>")
def logradouro(cep):
    logradouro = cep_to_logradouro(cep)
    if logradouro != ValueError:
        return {'logradouro': logradouro}
    return {
        'erro':     f'O CEP informado esta incorreto.',
        'codigo':   f'{500}',
        'cep':      f'{cep}'
        }

# --> --> --> --> --> --> --> --> --> --> -->
#           • Ajustes pendentes •
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

# --> --> --> --> --> --> --> --> --> --> -->
#          • Área de atendimento •
#
# O meu servidor tem uma URL bairro/cep
# Eu (Browser) --> meu servidor --> viacep
#
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

bairros_atende = ["Barra Funda", "Lapa", "Parque Residencial da Lapa", "Vila Invernada"]
@app.route("/atende/<cep>")
def atende(cep):
    bairro = cep_to_bairro(cep)
    return {"atende": bairro in bairros_atende, "status": "ok"}

#adiciona um bairro, pra eu nao precisar ficar mexendo no codigo pra adicionar
#bairros. Mas isso eu vou mostrar mais pra frente (se quiser brincar com isso
# aprenda primeiro como funciona a biblioteca requests)
@app.route("/bairros/<nome>", methods=["PUT"])
def add_bairro(nome):
    if nome not in bairros_atende:
        bairros_atende.append(nome)
        return {"bairro_adicionado": nome, "status": "ok"}
    #TODO: adicionar tratamento de erro se o bairro já está na lista. Status code 400.

#TODO adicionar remoção de bairro

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)
