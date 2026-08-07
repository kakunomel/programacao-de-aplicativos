import sqlite3

def cadastrar_professor():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_professor TEXT,
                    cpf_professor TEXT UNIQUE,
                    materia_professor TEXT) ''')

print("Tabela criada com sucesso!")
cadastrar_professor()