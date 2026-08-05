import sqlite3

def tabela_cinema():
    conexao = sqlite3.connect('sistema_cinemas.db')
    cursor = conexao.cursor()
    cursor.execute ('''
                    CREATE TABLE IF NOT EXISTS cinemas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_cinema TEXT NOT NULL,
                    shopping TEXT NOT NULL)''')

    