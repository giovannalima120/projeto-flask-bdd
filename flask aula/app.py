from flask import Flask, render_template, jsonify, request
import sqlite3


from dao import get_all_users, insert_user, select_user_by_id, delete_user_by_id, update_user_email_by_id

app = Flask(__name__)

def get_db_connection():
    conexao = sqlite3.connect("meu_banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao

# http://localhost:5000/usuarios
@app.route("/usuarios")
def listar_usuarios():
    usuarios = get_all_users() 
    return jsonify(usuarios)

# http://localhost:5000/usuarios/1
@app.route("/usuarios/<int:id>")
def recuperar_usuario(id):
    usuario = select_user_by_id(id) 
    return jsonify(usuario)

# http://localhost:5000/usuarios
@app.route("/usuarios", methods = ['POST'])
def criar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    usuario = insert_user(nome, email) 
    return f"Dados recebidos!"


# rotas adicionadas

# http://localhost:5000/usuarios/1
@app.route("/usuarios/<int:id>", methods = ['DELETE']) 
def deletar_usuario(id):
    delete_user_by_id(id)

# http://localhost:5000/usuarios/1
@app.route("/usuarios/<int:id>", methods = ['PUT']) 
def atualizar_usuario(id):
    data = request.get_json()
    email = data.get('email')
    update_user_email_by_id(id, email)



if __name__ == '__main__':
    app.run(debug=True)
