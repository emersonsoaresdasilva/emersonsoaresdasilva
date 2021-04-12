import requests

session = requests.Session()
token = '420dc72dadcadfba9adec9ea0e78faa94c87f1a8bf2b526572eccea4a3ce8550'
site_sptrans = 'http://api.olhovivo.sptrans.com.br/v2.1'

def retorna_dicionario(url):
    return (session.get(url).json() if conecta_sptrans(token) else {})

def conecta_sptrans(token):
    # Montando a URL para requisição http.
    url = f'{site_sptrans}/Login/Autenticar?token={token}' 
    # Retorna o status_code 200 indicando sucesso na conexão.
    return (session.post(url).status_code == 200)

def terminais_da_linha(codigo_linha):
    url = f'{site_sptrans}/Linha/Buscar?termosBusca={codigo_linha}'
    dicionario = retorna_dicionario(url)[0]
    terminal_principal = dicionario['tp']
    terminal_secundario = dicionario['ts']
    return f'''Terminal Principal: {terminal_principal} para Terminal Secundário: {terminal_secundario}'''

# print(terminais_da_linha('978T'))

def buscar_linha_sentido(codigo_linha, sentido):
    url = f'{site_sptrans}/Linha/BuscarLinhaSentido?termosBusca={codigo_linha}&sentido={sentido}'
    dicionario = retorna_dicionario(url)[0]
    terminal_principal = dicionario['tp']
    terminal_secundario = dicionario['ts']
    if sentido == 1: # 1: Terminal Principal para Terminal Secundário.
        return f'''{codigo_linha} - Terminal Principal: {terminal_principal} sentido: {terminal_secundario}''' 
    else: # 2: para Terminal Secundário para Terminal Principal.
        return f'''{codigo_linha} - Terminal Secundário: {terminal_secundario} sentido: {terminal_principal}'''

# print(buscar_linha_sentido('978T', 1))
# print(buscar_linha_sentido('978T', 2))

def exibe_corredores_inteligentes():
    url = f'{site_sptrans}/Corredor'
    dicionario = retorna_dicionario(url)
    for i in range(len(dicionario)):
        codigo_corredor = dicionario[i]['cc']
        nome_do_corredor = dicionario[i]['nc']
        print(f'''Código: {codigo_corredor} --> Nome do corredor: {nome_do_corredor}''')

# exibe_corredores_inteligentes()