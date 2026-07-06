from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Projeto
from flask import redirect

app = Flask(__name__)
CORS(app)

swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "API MVP Backend",
        "version": "1.0.0"
    }
})

engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@app.route('/projetos', methods=['POST'])
def criar_projeto():
    """
    Cadastra um novo projeto
    ---
    parameters:
      - in: body
        name: projeto
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
              example: Projeto Teste
            stack:
              type: string
              example: Python
            repo_url:
              type: string
              example: https://github.com/igoraraujocunha
    responses:
      201:
        description: Sucesso
    """
    dados = request.json
    if not dados or not dados.get('titulo'):
        return jsonify({"erro": "Payload inválido ou título ausente"}), 400

    with Session() as session:
        projeto = Projeto(
            titulo=dados['titulo'],
            stack=dados.get('stack'),
            repo_url=dados.get('repo_url')
        )
        session.add(projeto)
        session.commit()
        return jsonify({"mensagem": "Projeto cadastrado com sucesso"}), 201

@app.route('/projetos', methods=['GET'])
def listar_projetos():
    """
    Lista projetos
    ---
    responses:
      200:
        description: Lista de projetos
    """
    with Session() as session:
        projetos = session.query(Projeto).all()
        resultado = [{
            "id": p.id, 
            "titulo": p.titulo, 
            "stack": p.stack, 
            "repo_url": p.repo_url
        } for p in projetos]
        return jsonify(resultado), 200

@app.route('/projetos/<int:id>', methods=['GET'])
def buscar_projeto(id):
    """
    Busca projeto por ID
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Sucesso
      404:
        description: Não encontrado
    """
    with Session() as session:
        projeto = session.query(Projeto).filter(Projeto.id == id).first()

        if not projeto:
            return jsonify({"erro": "Projeto não encontrado"}), 404

        return jsonify({
            "id": projeto.id,
            "titulo": projeto.titulo,
            "stack": projeto.stack,
            "repo_url": projeto.repo_url
        }), 200

@app.route('/projetos/<int:id>', methods=['DELETE'])
def deletar_projeto(id):
    """
    Remove projeto
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Sucesso
      404:
        description: Não encontrado
    """
    with Session() as session:
        projeto = session.query(Projeto).filter(Projeto.id == id).first()

        if not projeto:
            return jsonify({"erro": "Projeto não encontrado"}), 404

        session.delete(projeto)
        session.commit()
        return jsonify({"mensagem": "Projeto removido"}), 200

@app.route('/')
def index():
    return redirect('/apidocs/')

if __name__ == '__main__':
    app.run(debug=True)