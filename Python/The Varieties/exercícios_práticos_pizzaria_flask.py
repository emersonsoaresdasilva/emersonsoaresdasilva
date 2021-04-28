''' 
from flask import Flask 
app = Flask(__name__)
  
@app.route("/")
def hello():
   return "Ola Mundo!"

if __name__ == '__main__':
   app.run(host = 'localhost', port = 5002, debug=True)
'''

from flask import Flask        
app = Flask(__name__)         
from flask import jsonify
from flask import request

pizzas = ['atum', 'marguerita', 'camarao']

# Início:
@app.route('/')
def hello():
   return 'Pizzaria!'

# Retorna lista de pizzas:
@app.route('/pizzas/')
def lista():
    return jsonify(pizzas)

# Consulta de pizza por nome:
@app.route('/pizzas/<nome>', methods=['GET'])
def busca_pizza_nome(nome):
    if nome not in pizzas:
        return jsonify({'resultado': 'não achei'}), 404
    return jsonify({'resultado': 'achei', 'sabor': nome})

# A mesma consulta da pizza, só que por ID:
@app.route('/pizzas/<int:id>', methods=['GET'])
def busca_pizza_id(id):
    if id >= len(pizzas):
        return jsonify({'resultado': 'não achei'}), 404
    return jsonify({'resultado': 'achei', 'sabor': pizzas[id]})

# Adiciona uma nova pizza:
@app.route('/pizzas/<nome>', methods=['PUT'])
def add_pizza(nome):
    if nome in pizzas:        
        return jsonify({'status': 'pizza ja existia'})
    pizzas.append(nome) 
    return jsonify({'status': 'ok'}), 201

# Remove pizza por nome:
@app.route('/pizzas/<nome>', methods=['DELETE'])
def remover_pizza_nome(nome):
    if nome not in pizzas:
        return  jsonify({'erro': 'pizza não existe'}), 400
    pizzas.remove(nome)
    return jsonify(pizzas)

# Remove pizza por id:
@app.route('/pizzas/<int:id>', methods=['DELETE'])
def remover_pizza_id(id):
    if id >= len(pizzas):
        return jsonify({'resultado': 'não achei'}), 404
    pizzas.remove(pizzas[id])
    return jsonify(pizzas)

# Recebe um dicionário de pedidos e diz se é valido ou não:
@app.route('/pedido', methods=['POST'])
def pedido():
    dicionario_retornado = request.json # Pegando o arquivo json, que o cliente enviou com os dados do pedido.
    for nome_pizza in dicionario_retornado.keys():
        if nome_pizza not in pizzas:
            return jsonify({'status': 'pedido contém alguma pizza inválida'}, 400) # {"sorvete": 2, "camarao": 1}
        else:
            return jsonify({'status': 'ok'}) # {"atum": 1, "marguerita": 2}
 
if __name__ == '__main__':     
   app.run(host = 'localhost', port = 6002, debug = True)
