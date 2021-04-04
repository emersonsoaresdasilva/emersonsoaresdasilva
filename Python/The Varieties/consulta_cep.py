import requests
from flask import Flask, jsonify

# Brincando com python...
# Usa a biblioteca requests para abrir uma conexao com o viacep.
def search(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    if requests.get(url).status_code == 200:
        return requests.get(url).json()
    return ValueError

def cep_to_bairro(cep):
    if search(cep) != ValueError:
        return search(cep)['bairro']
    return ValueError

def cep_to_logradouro(cep):
    if search(cep) != ValueError:
        return search(cep)['logradouro']
    return ValueError

# Gerar um objeto chamado app, uma burocracia que a gente faz sempre.
app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <div style="font-family:verdana">
            <p>Webservice gratuito para pesquisa de endereço <strong>via CEP.</strong></p>
            <ul>
                <li>/bairro/<strong>cep</strong></li>
                <li>/logradouro/<strong>cep</strong></li>
                <li>/atende/<strong>cep</strong></li>
                <li>/bairros/adicionar/<strong>nome</strong></li>
                <li>/bairros/deletar/<strong>nome</strong></li>
            </ul>
        </div>
    ''' # Não faça isso, carregar html não é uma boa prática, crie um arquivo index.html > seu código.

# --> --> --> --> --> --> --> --> --> --> -->
#               • Bairro / Rua •
#
# O meu servidor tem uma URL /bairro/<cep> ; /logradouro/<cep>
# Eu (Browser) --> meu servidor --> viacep
#
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

@app.route("/bairro/<cep>")
def bairro(cep):
    bairro = cep_to_bairro(cep)
    if bairro != ValueError:
        return jsonify({'bairro': bairro})
    return jsonify({'erro': 'O CEP informado esta incorreto.', 'codigo': f'{500}'})

@app.route("/logradouro/<cep>")
def logradouro(cep):
    logradouro = cep_to_logradouro(cep)
    if logradouro != ValueError:
        return jsonify({'logradouro': logradouro})
    return jsonify({'erro': 'O CEP informado esta incorreto.', 'codigo': f'{500}'})    

# --> --> --> --> --> --> --> --> --> --> -->
#          • Área de atendimento •
#
# O meu servidor tem uma URL /atende/<cep>
# Eu (Browser) --> meu servidor --> viacep
#
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

atende_bairros = ["Barra Funda", "Lapa", "Bela Vista", "Bom Retiro"]

@app.route("/atende/<cep>")
def atende(cep):
    bairro = cep_to_bairro(cep)
    logradouro = cep_to_logradouro(cep)
    if bairro != ValueError:
        if bairro in atende_bairros:
            return jsonify({'logradouro': logradouro, 'atende': bairro, 'status': 'ok'})
        return jsonify({'logradouro': logradouro, 'atende': bairro, 'status': 'Fora da area de atendimento'})
    return jsonify({'erro': 'O CEP informado esta incorreto.', 'codigo': f'{500}'})

# --> --> --> --> --> --> --> --> --> --> -->
#      • Adicionar bairro de atendimento •
#
# O meu servidor tem uma URL /bairros/adicionar/<nome>
# Eu (Browser) --> meu servidor --> viacep
#
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

# Adiciona um bairro, para eu não precisar ficar mexendo no codigo pra adicionar bairros.
@app.route("/bairros/adicionar/<nome>")
def add_bairro(nome):
    if nome not in atende_bairros:
        atende_bairros.append(nome)
        return jsonify({'bairro_adicionado': nome, 'status': 'ok'})
    return jsonify({'erro': 'O bairro informado esta na lista.', 'codigo': f'{400}'})

# --> --> --> --> --> --> --> --> --> --> -->
#      • Remover bairro de atendimento •
#
# O meu servidor tem uma URL /bairros/deletar/<nome>
# Eu (Browser) --> meu servidor --> viacep
#
# <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--

# Remove um bairro, para eu não precisar ficar mexendo no codigo pra remover bairros.
@app.route("/bairros/deletar/<nome>")
def delete_bairro(nome):
    if nome in atende_bairros:
        atende_bairros.remove(nome)
        return jsonify({'bairro_removido': nome, 'status': 'ok'})
    return jsonify({'erro': 'O bairro informado nao esta na lista.', 'codigo': f'{400}'})

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
