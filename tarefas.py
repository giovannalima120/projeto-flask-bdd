import sqlite3

conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        concluida INTEGER DEFAULT 0
        );
    '''
)



conn.commit()


def adicionarTarefa(titulo):
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

def marcarComoConcluida(id):
    cursor.execute(
        '''
            UPDATE tarefas
            set concluida = 1
            WHERE id = ?;
        '''
        , (id, )
    )
    conn.commit()

def removerTarefa(id):
    cursor.execute(
        '''
            DELETE FROM tarefas
            WHERE id = ?;
        '''
        , (id, )
    )
    conn.commit()

if __name__ == "__main__":
    while True:
        print("\n --- MENU ---" \
        "\n1 - Adicionar tarefa" \
        "\n2 - Listar tarefas" \
        "\n3 - Marcar tarefa como concluída" \
        "\n4 - Remover tarefa" \
        "\n0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título da tarefa: ")
            adicionarTarefa(titulo)
        elif opcao == "2":
            listarTarefas()
        elif opcao == "3":
            idTarefa = int(input("Digite o ID da tarefa: "))
            marcarComoConcluida(idTarefa)
        elif opcao == "4":
            idTarefa = int(input("Digite o ID da tarefa: "))
            removerTarefa(idTarefa)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

        