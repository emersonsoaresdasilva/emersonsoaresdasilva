import requests
from dataclasses import dataclass

"""
Instruções para TODOS os exercícios/funções abaixo:
1. Veja as instruções de como instalar o treinador e os testes no documento entregue junto com este arquivo.
2. Se um determinado parâmetro de uma função deve ser inteiro, então esta função deve rejeitar valores não-numéricos ou numerais não-inteiros nesse parâmetro.
3. Da mesma forma, se um parâmetro de uma função deve ser uma string, então esta função deve rejeitar valores que não sejam do tipo string nesse parâmetro.
4. Strings em branco são sempre consideradas inválidas.
5. Se algum dos parâmetros ser inválido, uma ValueError deve ser lançada. Recomenda-se usar as funções check_int e check_str acima para ajudar na validação.
6. Em todos os casos onde procura-se algum tipo de pokémon pelo nome ou pelo número e o mesmo não existir, uma exceção PokemonNaoExisteException deve ser lançada.
7. Em todos os casos onde procura-se algum treinador cadastrado e o mesmo não existir, uma exceção TreinadorNaoCadastradoException deve ser lançada.
8. Em todos os casos onde procura-se algum pokémon cadastrado e o mesmo não existir, uma exceção PokemonNaoCadastradoException deve ser lançada.
9. Em todos os casos onde tenta-se cadastrar um pokémon e o mesmo já exista, uma exceção PokemonJaCadastradoException deve ser lançada.
10. Todos os nomes de pokémons que aparecerem como parâmetros devem ser aceitos em minúsculas, MAIÚSCULAS ou até mesmo MiStUrAdO. Lembre-se dos métodos lower() e upper() da classe string.
11. Todos os nomes de pokémons, cores, jogos, movimentos, etc. recebidos e devolvidos pela PokeAPI estão em letras minúsculas e assim devem ser mantidas.

Alguns exemplos de URLs que podem servir de inspiração:
http://pokeapi.co/api/v2/

http://pokeapi.co/api/v2/pokemon/39/
http://pokeapi.co/api/v2/pokemon/jigglypuff/

http://pokeapi.co/api/v2/pokemon-species/39/
http://pokeapi.co/api/v2/pokemon-species/jigglypuff/

http://pokeapi.co/api/v2/evolution-chain/11/
http://pokeapi.co/api/v2/growth-rate/1/
http://pokeapi.co/api/v2/pokemon-color/2/
"""
"""
Não altere estas URLs. Elas são utilizadas para conectar no treinador e no PokeAPI, respectivamente.
"""
site_treinador = "http://127.0.0.1:9000"
site_pokeapi = "https://pokeapi.co"
"""
Vamos precisar destas quatro exceções personalizadas.

Abaixo, criamos excessões com nomes personalizados.
"""

class PokemonNaoExisteException(Exception):
    pass

class PokemonNaoCadastradoException(Exception):
    pass

class TreinadorNaoCadastradoException(Exception):
    pass

class PokemonJaCadastradoException(Exception):
    pass

"""
Esta função certifica-se de que seu parâmetro é um número inteiro e lança uma ValueError se não for.
"""
def check_int(a):
    if type(a) is not int:
        raise ValueError()
"""
Esta função certifica-se de que seu parâmetro é uma string e que não está vazia e lança uma ValueError se não for.
"""
def check_str(a):
    if type(a) is not str or a == "":
        raise ValueError()
"""
Esta classe será utilizada no exercício 12 abaixo.
"""
@dataclass()
class Pokemon:
    nome_treinador: str
    apelido: str
    tipo: str
    experiencia: int
    nivel: int
    cor: str
    evoluiu_de: str

"""
0. Funções auxiliares.
"""
def retorna_dicionario(url):
    return requests.get(url).json() if (requests.get(url).status_code == 200) else {}
"""
1. Dado o número de um pokémon, qual é o nome dele?
"""
def nome_do_pokemon(numero):
    url = f"{site_pokeapi}/api/v2/pokemon/{numero}"
    dicionario_retornado = retorna_dicionario(url)
    if dicionario_retornado:
        return dicionario_retornado['name']
    raise PokemonNaoExisteException
"""
2. Dado o nome de um pokémon, qual é o número dele?
"""
def numero_do_pokemon(nome):
    url = f"{site_pokeapi}/api/v2/pokemon/{nome}/".lower()
    dicionario_retornado = retorna_dicionario(url)
    if dicionario_retornado:
        return dicionario_retornado['id']
    raise PokemonNaoExisteException
"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?
"""
def color_of_pokemon(nome):
    id = numero_do_pokemon(nome) # A partir do nome do pokemon, retorna o id do mesmo.
    url = f'{site_pokeapi}/api/v2/pokemon-species/{id}/' # Características do pokemon.
    dicionario_retornado = retorna_dicionario(url)
    if dicionario_retornado:
        return dicionario_retornado['color']['name']
    raise PokemonNaoExisteException
"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?
"""
def cor_do_pokemon(nome):
    traducao_de_cores = {
        "brown":    "marrom",
        "yellow":   "amarelo",
        "blue":     "azul",
        "pink":     "rosa",
        "gray":     "cinza",
        "purple":   "roxo",
        "red":      "vermelho",
        "white":    "branco",
        "green":    "verde",
        "black" :   "preto"}
    cor = color_of_pokemon(nome).lower()
    if cor in traducao_de_cores:
        return traducao_de_cores[cor]
    raise PokemonNaoExisteException
"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.
"""
def tipos_do_pokemon(nome):
    traducao_de_tipos = {
        "normal":      "normal",
        "fighting":    "lutador",
        "flying":      "voador",
        "poison":      "veneno",
        "ground":      "terra",
        "rock":        "pedra",
        "bug":         "inseto",
        "ghost":       "fantasma",
        "steel":       "aço",
        "fire":        "fogo",
        "water":       "água",
        "grass":       "grama",
        "electric":    "elétrico",
        "psychic":     "psíquico",
        "ice":         "gelo",
        "dragon":      "dragão",
        "dark":        "noturno",
        "fairy":       "fada"}
    url = f"{site_pokeapi}/api/v2/pokemon/{nome}/".lower()
    dicionario_retornado = retorna_dicionario(url)
    tipos_de_pokemon = []
    if dicionario_retornado:
        for item in dicionario_retornado['types']:
            chave_english = item['type']['name']
            tipos_de_pokemon.append(traducao_de_tipos[chave_english])
        return tipos_de_pokemon
    raise PokemonNaoExisteException
"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None
"""
def evolucao_anterior(nome):
    id = numero_do_pokemon(nome) # A partir do nome do pokemon, retorna o id do mesmo.
    url = f"{site_pokeapi}/api/v2/pokemon-species/{id}/" # Características do pokemon.
    dicionario_retornado = retorna_dicionario(url)
    if dicionario_retornado:
        if dicionario_retornado['evolves_from_species']:
            return dicionario_retornado['evolves_from_species']['name']
        return None
    raise PokemonNaoExisteException
"""
7. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evolutivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []

O exercicio 7 é opcional e bastante dificil. Se quiser, desligue os testes e vá para o 8!
"""
def mapear_proximas_evolucoes(cadeia_evolutiva, especie_atual, evolucoes):
    proximas_cadeias = cadeia_evolutiva['evolves_to']
    if cadeia_evolutiva['species']['name'] == especie_atual:
        for cadeia in proximas_cadeias:
            evolucoes.append(cadeia['species']['name'])
    elif len(proximas_cadeias) == 1:
        mapear_proximas_evolucoes(proximas_cadeias[0],especie_atual, evolucoes)
    else:
        # Quando uma espécie pode evoluir para N espécies, nenhuma destas N espécies possuem uma próxima espécie para evoluir.
        return [] 

def evolucoes_proximas(nome):
    evolucoes = []
    especie_atual = nome.lower()
    id = numero_do_pokemon(especie_atual)
    url_especie = f"{site_pokeapi}/api/v2/pokemon-species/{id}/"
    dados_especie = retorna_dicionario(url_especie)
    cadeia_evolutiva = retorna_dicionario(dados_especie['evolution_chain']['url'])['chain']      
    mapear_proximas_evolucoes(cadeia_evolutiva, especie_atual, evolucoes)
    return evolucoes
"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
"""
def nivel_do_pokemon(nome, experiencia):
    id = numero_do_pokemon(nome) # A partir do nome do pokemon, retorna o id do mesmo.
    url = f'{site_pokeapi}/api/v2/pokemon-species/{id}/' # Características do pokemon.
    dicionario_retornado = retorna_dicionario(url)
    if dicionario_retornado:        
        growth_rate = dicionario_retornado['growth_rate']['name']
        url = f'{site_pokeapi}/api/v2/growth-rate/'
        dicionario_retornado = retorna_dicionario(url)
        lista_de_growth_rates = dicionario_retornado['results']
        for i in range(len(lista_de_growth_rates)):
            if lista_de_growth_rates[i]['name'] == growth_rate:
                url = lista_de_growth_rates[i]['url']
                dicionario_retornado = retorna_dicionario(url)
                lista_de_levels = dicionario_retornado['levels']
                for i in range(len(lista_de_levels)):
                    if experiencia < lista_de_levels[i]['experience']:
                        return lista_de_levels[i-1]['level']
                    elif lista_de_levels[i]['experience'] == experiencia:
                        return lista_de_levels[i]['level']
                return lista_de_levels[i]['level']
    raise PokemonNaoExisteException
"""
A partir daqui, você precisará rodar o servidor treinador.py na sua máquina para poder
fazer a atividade. Não precisa mexer no arquivo, basta rodar ele.

Os testes relativos ao treinador.py estao no arquivo pokemon_treinador_unittest.py
"""
# Funcões auxiliares (treinador).
def existe_treinador(nome_treinador):
    return (requests.get(f'{site_treinador}/treinador/{nome_treinador}').status_code != 200)

def existe_pokemon(nome_treinador, apelido_pokemon):
    return (requests.get(f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}').status_code != 200)
"""
9. Dado um nome de treinador, cadastre-o na API de treinador.
Retorne True se um treinador com esse nome foi criado e False em caso contrário (já existia).

Dicas teste 9: Use o verbo PUT, URL {site_treinador}/treinador/{nome}
para criar um treinador. Se ele já existe, será retornado um cod de status
303. Se não existe, cod status 202.
"""
def cadastrar_treinador(nome):
    return ((requests.put(f'{site_treinador}/treinador/{nome}')).status_code == 202)
"""
10. Imagine que você capturou dois pokémons do mesmo tipo. Para diferenciá-los, você dá nomes diferentes (apelidos) para eles.
Logo, um treinador pode ter mais do que um pokémon de um determinado tipo, mas não pode ter dois pokémons diferentes com o mesmo apelido.

Dados: um nome de treinador, um apelido de pokémon, um tipo de pokémon e uma quantidade de experiência, 

cadastre o pokémon com o tipo correspondente, na lista do treinador que foi passado, usando a API (o servidor) do treinador.
Certifique-se de que todos os dados são válidos.

Inicio teste 10 -- para passar o 10a
* Para cadastrar um pokemon, usar a url {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}, enviando um arquivo json com a chave tipo (por exemplo tipo=pikachu) e a chave experiência
* Para enviar um dicionario pra uma URL, usando o verbo put
requests.put(url,json = {"tipo":"pikachu","experiencia"...})

Mais dicas teste 10: 
* Pode ser necessário usar a pokeapi para verificar se um pokemon existe -- se eu falar que o geremias é dono de um pokemon do tipo homer, deve ocorrer uma excessao, porque homer não é uma espécie válida de pokemon
* Se voce receber um status 404, isso indica um treinador nao encontrado
* Se voce receber um status 409, isso indica que o pokemon já existia e você
está fazendo um cadastro dobrado
* Se voce receber um status 202, isso indica criação bem sucedida
"""
def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    url = f"{site_pokeapi}/api/v2/pokemon/{tipo_pokemon}/".lower()
    if (requests.get(url).status_code == 404):
        raise PokemonNaoExisteException
    else:
        url = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}'
        envia_dicionario = requests.put(url, json = {"tipo": tipo_pokemon, "experiencia": experiencia})
        if envia_dicionario.status_code == 404:
            raise TreinadorNaoCadastradoException
        elif envia_dicionario.status_code == 409:
            raise PokemonJaCadastradoException
    return True
"""
11. Dado um nome de treinador, um apelido de pokémon e uma quantidade de experiência, localize esse pokémon e acrescente-lhe a experiência ganha.

Dicas ex 11:
utilize a URL {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}/exp
Por exemplo, se for o pokemon com apelido terra
do treinador lucas, a URL ficaria: {site_treinador}/treinador/lucas/terra/exp

Utilize o verbo POST, enviando um arquivo json com a chave experiencia (o valor dessa chave é o tanto de exp que eu quero acrescentar)

Um cod de status 404 pode significar 2 coisas distintas: ou o treinador não existe,
ou o treinador existe mas o pokemon não. Isso pode verificado acessando a resposta.text
(em vez do usual, que seria resposta.json())

O cod de status de sucesso é o 204
"""
def ganhar_experiencia(nome_treinador, apelido_pokemon, experiencia):
    if existe_treinador(nome_treinador):
        raise TreinadorNaoCadastradoException
    elif existe_pokemon(nome_treinador, apelido_pokemon):
        raise PokemonNaoCadastradoException
    else:
        detalhes_site = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}/exp'
        requests.post(detalhes_site, json={'experiencia': experiencia})
    return experiencia
"""
12. Dado um nome de treinador e um apelido de pokémon, localize esse pokémon na API do treinador e retorne um objeto da classe Pokemon, prenchida com os atributos definidos na classe

Dicas 12:
pegar os dados na url "{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}"
acessada com o verbo GET
para preencher o objeto Pokemon, voce vai fornecer
* nome treinador (veio como argumento da funcao)
* apelido pokemon (veio como argumento da funcao)
* tipo (veio do get que você fez -- chave tipo do dicionário)
* experiencia (veio do request que você fez -- chave experiencia do dicionário)
* nivel do pokemon (calcular usando a pokeapi -- voce ja fez essa funcao, use ela)
* cor do pokemon (em portugues, pegar da pokeapi -- voce ja fez essa funcao, use ela)
* evolucao anterior (pegar da pokeapi -- voce ja fez essa funcao, use ela)
Retornar o objeto pokemon
Erros 404 podem ser treinador nao existe ou pokemon nao existe -- verifique resposta.text para ver qual dos dois -- já fizemos isso antes
"""
def localizar_pokemon(nome_treinador, apelido_pokemon):
    if existe_treinador(nome_treinador):
        raise TreinadorNaoCadastradoException
    elif existe_pokemon(nome_treinador, apelido_pokemon):
        raise PokemonNaoCadastradoException
    else:
        url = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}'
        dicionario_retornado = retorna_dicionario(url)
        nome = dicionario_retornado['tipo']
        experiencia = dicionario_retornado['experiencia']
        nivel = nivel_do_pokemon(nome, experiencia)
        cor = cor_do_pokemon(nome)
        evolucao = evolucao_anterior(nome)
    return Pokemon(nome_treinador, apelido_pokemon, nome, experiencia, nivel, cor, evolucao)
"""
13. Dado o nome de um treinador, localize-o na API do treinador e retorne um dicionário dos seus pokemons. As chaves do dicionário serão os apelidos dos pokémons dele, e os valores serão os tipos (pikachu, bulbasaur ...) deles.

Essas informações estão na URL "{site_treinador}/treinador/{nome_treinador}",
acessiveis com o verbo GET
Consulte ela com seu navegador e veja o que tem lá! (talvez você queira usar
as funções anteriores para criar um treinador e seus pokemons...)
"""
def detalhar_treinador(nome_treinador):
    if existe_treinador(nome_treinador):
        raise TreinadorNaoCadastradoException
    else:
        url = f'{site_treinador}/treinador/{nome_treinador}'
        dicionario_retornado = retorna_dicionario(url)['pokemons']
        if 'P' in dicionario_retornado:
            p_apelido = dicionario_retornado['P']['apelido']
            p_tipo = dicionario_retornado['P']['tipo']
            if 'Q' in dicionario_retornado:
                q_apelido = dicionario_retornado['Q']['apelido']
                q_tipo = dicionario_retornado['Q']['tipo']
                return {p_apelido: p_tipo, q_apelido: q_tipo}
            return {p_apelido: p_tipo}
"""
14. Dado o nome de um treinador, localize-o na API do treinador e exclua-o, juntamente com todos os seus pokémons.

Usar o verbo delete na url do treinador. A mesma que a gente já usou várias vezes.
O status code vai de informar se o treinador não existia (com qual status code?)
"""
def excluir_treinador(nome_treinador):
    if existe_treinador(nome_treinador):
        raise TreinadorNaoCadastradoException
    else:
        url = f'{site_treinador}/treinador/{nome_treinador}'
        return (requests.delete(url).status_code == 204)
"""
15. Dado o nome de um treinador e o apelido de um de seus pokémons, localize o pokémon na API do treinador e exclua-o.

Usar o verbo delete na url do pokemon: {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}
O status code vai de informar se o treinador não existe, ou se o pokemon nao existe 
(status code 404, não deixe de verificar se foi o pokemon ou treinador que não existia)
"""
def excluir_pokemon(nome_treinador, apelido_pokemon):
    if existe_treinador(nome_treinador):
        raise TreinadorNaoCadastradoException
    elif existe_pokemon(nome_treinador, apelido_pokemon):
        raise PokemonNaoCadastradoException
    else:
        url = f'{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}'
    return (requests.delete(url).status_code == 204)
