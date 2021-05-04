import requests

site_api = 'https://api.cpfcnpj.com.br'
token = 'C54A4C55-84C4-4902-AA55-EE0C48804D2C'

def retorna_dicionario(url):
    return requests.get(url).json() if (requests.get(url).status_code == 200) else {}

def consultar_cpf(cpf):
    url = f'{site_api}/{token}/9/{cpf}'
    dicionario_retornado = retorna_dicionario(url)
    return dicionario_retornado

print(consultar_cpf(''))