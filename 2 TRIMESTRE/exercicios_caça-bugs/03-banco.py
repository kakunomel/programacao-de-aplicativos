import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS escolas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT) ''')
    
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS series(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT,
                id_escola INTERGER,
                FOREIGN KEY (id_escola)REFERENCES escolas (id)) ''')

    conexao.commit()
    conexao.close()

#ESTAVA DANDO ERRO PORQUE ESTAVA PUXNDO UMA REFERÊNCIA DE UMA TABELA QUE NÃO EXISTE