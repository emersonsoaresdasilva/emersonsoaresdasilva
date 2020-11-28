#Utilizando pacotes externos.
import json
from pygeocoder import Geocoder
from funcoes_json import *

dicionario = {"endereco": ["Lins de Vasconcelos", "1222", "Aclimacao", "Sao Paulo", "SP"]}

dicionario = ler_arquivo("entrada.json")
lista = dicionario["endereco"]
endereco = lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
saida = {"coordenadas": Geocoder.geocode(endereco).coordinates}
gravar_arquivo(saida, "saida.json")