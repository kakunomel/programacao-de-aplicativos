import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escolaa.db')
    cursor = conexao.cursor

    cursor.executemany("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro))

    print(cursor.fetchone())
    conexao.close()

buscar_dados_dinamicos(nome_tabela, id_registro)