import sqlite3 

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS escolas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL )
                ''')

    #O BANCO NÃO ESTÁ SALVANDO AS ALTERAÇÕES. POE QUÊ?
    #O BANCO DE DADOS NÃO TINHA SIDO CRIADO
    conexao.commit()
    conexao.close()