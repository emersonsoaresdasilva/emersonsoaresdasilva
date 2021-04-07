import requests

def pega_cidade(ip):
    url = f'http://sys.airtel.lv/ip2country/{ip}/?full=true'
    cidade = requests.get(url).json()['city']
    return f'Cidade do IP é: {cidade}'

# print(pega_cidade('182.21.6.20')) --> Digite seu ip.