import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS escolas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL)
                    ''')

#O BANCO NÃO ESTÁ SAVANDO AS ALTERAÇÕES. POR QUÊ?
conexao.close()