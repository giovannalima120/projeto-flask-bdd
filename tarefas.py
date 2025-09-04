import sqlite3

def criarTabela():
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
    conn.close()


def adicionarTarefa(titulo):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tarefas (titulo, concluida) VALUES (?, ?); 
    '''
    , (titulo, 0)
    )

    conn.commit()
    conn.close()

def listarTarefas():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT * FROM tarefas;
'''
    )
    tarefas = cursor.fetchall()
    conn.close()
    return [{"id": t[0], "titulo": t[1], "concluida": t[2]} for t in tarefas] 

def marcarComoConcluida(id):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
            UPDATE tarefas
            set concluida = 1
            WHERE id = ?;
        '''
        , (id, )
    )
    conn.commit()
    conn.close()

def removerTarefa(id):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
            DELETE FROM tarefas
            WHERE id = ?;
        '''
        , (id, )
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criarTabela()
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
            tarefas = listarTarefas()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("\n--- LISTA DE TAREFAS ---")
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} {t['concluida']}")
            input("\nPressione ENTER para voltar ao menu.")
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

        