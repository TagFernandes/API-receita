from flask import Blueprint, request, jsonify
from models import db, Ingrediente, Receita, ReceitaIngrediente

bp = Blueprint('api', __name__)

# ----------- INGREDIENTES -----------

@bp.route('/ingredientes', methods=['POST'])
def criar_ingrediente():
    data = request.json
    ingrediente = Ingrediente(nome=data['nome'], unidade=data['unidade'])
    db.session.add(ingrediente)
    db.session.commit()
    return jsonify({'id': ingrediente.id}), 201

@bp.route('/ingredientes', methods=['GET'])
def listar_ingredientes():
    nome = request.args.get('nome')
    if nome:
        ingredientes = Ingrediente.query.filter(Ingrediente.nome.ilike(f'%{nome}%')).all()
    else:
        ingredientes = Ingrediente.query.all()

    return jsonify([
        {'id': i.id, 'nome': i.nome, 'unidade': i.unidade} for i in ingredientes
    ])


@bp.route('/ingredientes/<int:id>', methods=['GET'])
def obter_ingrediente(id):
    i = Ingrediente.query.get_or_404(id)
    return jsonify({'id': i.id, 'nome': i.nome, 'unidade': i.unidade})

@bp.route('/ingredientes/<int:id>', methods=['PUT'])
def atualizar_ingrediente(id):
    data = request.json
    i = Ingrediente.query.get_or_404(id)
    i.nome = data['nome']
    i.unidade = data['unidade']
    db.session.commit()
    return jsonify({'mensagem': 'Ingrediente atualizado'})

@bp.route('/ingredientes/<int:id>', methods=['DELETE'])
def deletar_ingrediente(id):
    ingrediente = Ingrediente.query.get_or_404(id)

    # Verifica se está associado a alguma receita
    associacoes = ReceitaIngrediente.query.filter_by(ingrediente_id=ingrediente.id).all()

    if associacoes:
        # Pega os IDs das receitas associadas
        receitas_ids = {assoc.receita_id for assoc in associacoes}
        receitas = Receita.query.filter(Receita.id.in_(receitas_ids)).all()

        return jsonify({
            'mensagem': 'Ingrediente está associado a receitas e não pode ser deletado.',
            'receitas_associadas': [
                {'id': r.id, 'nome': r.nome} for r in receitas
            ]
        }), 400

    # Se não tiver associação, pode deletar
    db.session.delete(ingrediente)
    db.session.commit()
    return jsonify({'mensagem': 'Ingrediente deletado com sucesso.'})



# ----------- RECEITAS -----------

@bp.route('/receitas', methods=['POST'])
def criar_receita():
    data = request.json
    receita = Receita(nome=data['nome'], modo_preparo=data['modo_preparo'])
    db.session.add(receita)
    db.session.flush()

    ingredientes_nao_encontrados = []

    for item in data['ingredientes']:
        # Verifica se o ingrediente existe
        ingrediente = Ingrediente.query.get(item['id'])
        if not ingrediente:
            # Se não existir, adicionar à lista de ingredientes não encontrados
            ingredientes_nao_encontrados.append(item['id'])
        else:
            # Caso o ingrediente exista, associar à receita
            ri = ReceitaIngrediente(
                receita_id=receita.id,
                ingrediente_id=item['id'],
                quantidade=item['quantidade']
            )
            db.session.add(ri)

    # Se algum ingrediente não foi encontrado, retornar erro
    if ingredientes_nao_encontrados:
        return jsonify({
            'erro': 'Ingredientes não cadastrados',
            'ingredientes_nao_encontrados': ingredientes_nao_encontrados
        }), 400

    db.session.commit()
    return jsonify({'id': receita.id}), 201



@bp.route('/receitas', methods=['GET'])
def listar_receitas():
    nome = request.args.get('nome')
    if nome:
        receitas = Receita.query.filter(Receita.nome.ilike(f'%{nome}%')).all()
    else:
        receitas = Receita.query.all()

    resultado = []
    for r in receitas:
        ingredientes = ReceitaIngrediente.query.filter_by(receita_id=r.id).all()
        resultado.append({
            'id': r.id,
            'nome': r.nome,
            'modo_preparo': r.modo_preparo,
            'ingredientes': [
                {'ingrediente_id': i.ingrediente_id, 'quantidade': i.quantidade}
                for i in ingredientes
            ]
        })
    return jsonify(resultado)


@bp.route('/receitas/<int:id>', methods=['GET'])
def obter_receita(id):
    r = Receita.query.get_or_404(id)
    ingredientes = ReceitaIngrediente.query.filter_by(receita_id=r.id).all()
    return jsonify({
        'id': r.id,
        'nome': r.nome,
        'modo_preparo': r.modo_preparo,
        'ingredientes': [
            {'ingrediente_id': i.ingrediente_id, 'quantidade': i.quantidade}
            for i in ingredientes
        ]
    })

@bp.route('/receitas/<int:id>', methods=['PUT'])
def atualizar_receita(id):
    data = request.json
    r = Receita.query.get_or_404(id)
    r.nome = data['nome']
    r.modo_preparo = data['modo_preparo']
    
    # Limpar os ingredientes anteriores antes de adicionar os novos
    ReceitaIngrediente.query.filter_by(receita_id=r.id).delete()

    ingredientes_nao_encontrados = []

    for item in data['ingredientes']:
        # Verifica se o ingrediente existe
        ingrediente = Ingrediente.query.get(item['id'])
        if not ingrediente:
            # Se não existir, adicionar à lista de ingredientes não encontrados
            ingredientes_nao_encontrados.append(item['id'])
        else:
            # Caso o ingrediente exista, associar à receita
            ri = ReceitaIngrediente(
                receita_id=r.id,
                ingrediente_id=item['id'],
                quantidade=item['quantidade']
            )
            db.session.add(ri)

    # Se algum ingrediente não foi encontrado, retornar erro
    if ingredientes_nao_encontrados:
        return jsonify({
            'erro': 'Ingredientes não cadastrados',
            'ingredientes_nao_encontrados': ingredientes_nao_encontrados
        }), 400

    db.session.commit()
    return jsonify({'mensagem': 'Receita atualizada com sucesso'})


@bp.route('/receitas/<int:id>', methods=['DELETE'])
def deletar_receita(id):
    r = Receita.query.get_or_404(id)
    ReceitaIngrediente.query.filter_by(receita_id=r.id).delete()
    db.session.delete(r)
    db.session.commit()
    return jsonify({'mensagem': 'Receita deletada'})


@bp.route('/health')
def health():
    return "Olá, Docker + Flask + PostgreSQL!"