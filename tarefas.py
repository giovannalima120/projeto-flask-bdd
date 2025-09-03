import sqlite3

conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL
        concluida INTEGER DEFAULT 0
        );
    '''
)



conn.commit()


def adicionarTarefa(titulo: str):
    cursor.execute('''
        INSERT INTO tarefas (titulo, concluida) VALUES (?, ?); 
    '''
    , (titulo, 0)
    )

    cursor.commit()
    conn.close()

def listarTarefas():
    cursor.execute(
        '''
        SELECT * FROM tarefas;
'''
    )
    tarefas = cursor.fetchall()
    tarefaDict = [dict(u) for u in tarefas]
    conn.close()
    return tarefaDict

def 
        