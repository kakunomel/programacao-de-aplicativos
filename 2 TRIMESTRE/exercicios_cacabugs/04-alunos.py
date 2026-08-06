import sqlite3

def tabela_alunos():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_aluno TEXT NOT NULL,
                id_turma INTEGER,
                FOREIGN KEY (id_turma) REFERENCES series (id))
                ''')
    conexao.commit()
    conexao.close()
    print("\nTabela criada com sucesso!\n")



def vincular_aluno_turma():
    nome_aluno = input("Nome do aluno: ")

    try:
        id_turma = int(input("Digite o ID da turma:"))
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome_aluno, id_turma) VALUES (?, ?)", (nome_aluno, id_turma))
        conexao.commit()
        print("Aluno cadastrado com sucesso!\n")

    except ValueError:
        print("\nErro: Digite apenas numeros!")
    
    except sqlite3.Error:
        print("\nErro no banco de dados!")
    
    finally:
        conexao.close()

tabela_alunos()
vincular_aluno_turma()