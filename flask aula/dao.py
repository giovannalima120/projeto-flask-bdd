import sqlite3

DATABASE ="meu_banco.db"

def get_db_connection():
     conexao = sqlite3.connect(DATABASE)
     conexao.row_factory = sqlite3.Row
     return conexao

# def create_user_table():
#     conexao = get_db_connection()
#     cursor = conexao.cursor()
#     cursor.execute(
#         '''
#             CREATE TABLE IF NOT EXISTS usuarios(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT NOT NULL,
#                 email TEXT NOT NULL UNIQUE
#             )
#         '''
#     )
#     conexao.commit()
#     conexao.close()

def insert_user(nome, email):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute(
        '''
            INSERT INTO usuarios(nome, email) VALUES (?, ?);
        '''
        , (nome, email)
    )
    cursor.commit()
    conexao.close()

def get_all_users():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute(
        '''
            SELECT * FROM usuarios;
        '''
    )
    usuarios = cursor.fetchall()
    # Converte formato ROW do sqlite3 para Dicionario 
    usuarioDict = [dict(u) for u in usuarios]
    conexao.close()
    return usuarioDict

def select_user_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
            SELECT * FROM usuarios WHERE id = ?;
        '''
        , (id, )
    )
    user = dict(cursor.fetchone())
    conn.close()
    return user

def insert_user(nome, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
            INSERT INTO usuarios (nome, email) 
            VALUES (?, ?)
        ''', (nome, email)
    )
    conn.commit()
    conn.close()

def delete_user_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
            DELETE FROM usuarios
            WHERE id = ?;
        '''
        , (id, )
    )
    conn.commit()
    conn.close()

def update_user_email_by_id(email, id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
            UPDATE usuarios 
            SET email = ?
            WHERE id = ?;
        '''
        , (email, id)
    )
    conn.execute()
    conn.close()
