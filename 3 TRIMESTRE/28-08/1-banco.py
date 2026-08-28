import sqlite3

def tabela_escolas():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")

    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_escola TEXT NOT NULL,
                nome_cidade TEXT NOT NULL) ''')
        conexao.commit()

    except sqlite3.Error as e:
        print("Erro..." , e)

    finally:
        conexao.close()



def tabela_turmas():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")

    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT NOT NULL,
                id_escola INTEGER,
                FOREIGN KEY (id_escola) REFERENCES escolas(id))''')
        conexao.commit()

    except sqlite3.Error as e:
        print("Erro..." , e)

    finally:
        conexao.close()



def tabela_alunos():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")

    try:
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_aluno TEXT NOT NULL,
                idade_aluno INTEGER,
                id_turma INTEGER,
                FOREIGN KEY (id_turma) REFERENCES turmas(id))''')
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro..." , e)

    finally:
        conexao.close()


tabela_escolas()
tabela_turmas()
tabela_alunos()

print("Tabelas criadas com sucesso!")