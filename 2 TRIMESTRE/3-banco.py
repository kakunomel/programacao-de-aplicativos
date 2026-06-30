import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #ESTE BLOCO QUEBRRA AO RODAR PELA PRIMEIRA VEZ EM UM BANCO LIMPO. POR QUÊ?
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS series(
                    id integer primary key autoincrement,
                    nome_serie TEXT,
                    id_escola INTEGER,
                    FOREN KEY (id_escola) REFERENCES escolas(id)) ''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTST escolas(
                    id INTEGER PRIMARY KEY AUTOINCREMEN,
                    nome TEXT) ''')
    conexao.commit()
    conexao.close()