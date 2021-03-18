import requests
from flask import Flask

# Usa a biblioteca requests para abrir uma conexao com o viacep.
def search_dados(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code != 200:
        return ValueError
    dicionario_retornado = response.json()
    return dicionario_retornado

def cep_to_logradouro(cep):
    return search_dados(cep)['logradouro'] 

def cep_to_bairro(cep):
    return search_dados(cep)['bairro']    

def cep_to_cidade(cep):
    return search_dados(cep)['localidade']

def cep_to_estado(cep):
    return search_dados(cep)['uf']

# Gerar um objeto chamado app, uma burocracia que a gente faz sempre.
app = Flask(__name__)

# --> --> --> --> --> --> --> --> --> --> -->
#               • Bairros •
#
# O meu servidor tem uma URL bairro/cep
# Eu (Browser) --> meu servidor --> viacep
#
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

@app.route("/bairro/<cep>")
def bairros(cep):
    bairro_logradouro = cep_to_logradouro(cep)
    bairro_local = cep_to_bairro(cep)
    bairro_cidade = cep_to_cidade(cep)
    bairro_estado = cep_to_estado(cep)

    return f'''
            <p style="font-family:verdana">Rua:         {bairro_logradouro} </p>
            <p style="font-family:verdana">Localização: {bairro_local}      </p>
            <p style="font-family:verdana">Cidade:      {bairro_cidade}     </p>
            <p style="font-family:verdana">Estado:      {bairro_estado}     </p>
        '''

# --> --> --> --> --> --> --> --> --> --> -->
#               • Atende •
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

# PAREI AQUI

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
