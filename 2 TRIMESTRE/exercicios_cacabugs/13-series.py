import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola))
        conexao.commit()

    except sqlite3.Error as e:
        print("Erro técnico:", e)
    finally:
        if conexao:
            conexao.close()

#SE A CONEXÃO FALHAR, ELA NÃO EXISTE EO 'FINALLY' TENTA FECHAR ALGO QUE NÃO FOI CRIADO