from flask import Flask, render_template, jsonify, request
import sqlite3

from dao import get_all_users, insert_user, select_user_by_id

app = Flask(__name__)

def get_db_connection():
    conexao = sqlite3.connect("meu_banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao

# http://localhost:5000/usuarios
@app.route("/usuarios")
def listar_usuarios():
    usuarios = get_all_users() # Importado de DAO
    # retornar os usuários
    return jsonify(usuarios)

# http://localhost:5000/usuarios/1
@app.route("/usuarios/<int:id>")
def recuperar_usuario(id):
    usuario = select_user_by_id(id) # Importado de DAO
    # retornar um único usuário
    return jsonify(usuario)

# http://localhost:5000/usuarios
@app.route("/usuarios", methods = ['POST'])
def criar_usuario():
    # Importar request de flask
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email') 
    # Importar insert_user de DAO
    usuario = insert_user(nome, email) 
    return f"Dados recebidos!"

if __name__ == '__main__':
    app.run(debug=True)
