from flask import Blueprint, request, jsonify

bp = Blueprint('api', __name__)

# ---------------- INGREDIENTES ----------------

@bp.route('/ingredientes', methods=['POST'])
def criar_ingrediente():
    data = request.json
    print("Ingrediente recebido:", data)
    return jsonify({'mensagem': 'Ingrediente recebido'}), 201

@bp.route('/ingredientes', methods=['GET'])
def listar_ingredientes():
    print("Listando ingredientes...")
    return jsonify({'mensagem': 'Listagem simulada de ingredientes'})

@bp.route('/ingredientes/<int:id>', methods=['GET'])
def obter_ingrediente(id):
    print(f"Buscando ingrediente com ID {id}")
    return jsonify({'mensagem': f'Retorno simulado do ingrediente {id}'})

@bp.route('/ingredientes/<int:id>', methods=['PUT'])
def atualizar_ingrediente(id):
    data = request.json
    print(f"Atualizando ingrediente {id} com dados:", data)
    return jsonify({'mensagem': f'Ingrediente {id} atualizado'})

@bp.route('/ingredientes/<int:id>', methods=['DELETE'])
def deletar_ingrediente(id):
    print(f"Deletando ingrediente com ID {id}")
    return jsonify({'mensagem': f'Ingrediente {id} deletado'})


# ---------------- RECEITAS ----------------

@bp.route('/receitas', methods=['POST'])
def criar_receita():
    data = request.json
    print("Receita recebida:", data)
    return jsonify({'mensagem': 'Receita recebida'}), 201

@bp.route('/receitas', methods=['GET'])
def listar_receitas():
    print("Listando receitas...")
    return jsonify({'mensagem': 'Listagem simulada de receitas'})

@bp.route('/receitas/<int:id>', methods=['GET'])
def obter_receita(id):
    print(f"Buscando receita com ID {id}")
    return jsonify({'mensagem': f'Retorno simulado da receita {id}'})

@bp.route('/receitas/<int:id>', methods=['PUT'])
def atualizar_receita(id):
    data = request.json
    print(f"Atualizando receita {id} com dados:", data)
    return jsonify({'mensagem': f'Receita {id} atualizada'})

@bp.route('/receitas/<int:id>', methods=['DELETE'])
def deletar_receita(id):
    print(f"Deletando receita com ID {id}")
    return jsonify({'mensagem': f'Receita {id} deletada'})
