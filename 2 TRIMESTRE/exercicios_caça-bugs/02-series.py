import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor

    #O ALUNO TENTA CADASTRAR UMA SÉRIE COM ID_ESCOLA = 999(QUE NÃO ESXISTE)
    #O SQLITE ACEITA O CADASTRO MESMO ASSIM. O QUE ESTÁ FALTANDO ATIVAR?
    #FALTAVA A VERIFICAÇÃO DE CHAVES

    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("INSERT INTO series(nome_serie, id_escola)VALUES (?, ?)", (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()