import sqlite3

def cadastrar_serie_seguro():
    conexao = None
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        nome_serie = input("Digite o nome da série: ")
        id_escola = int(input("Digite o ID da escola: "))

        cursor.execute( "INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome_serie, id_escola))
        conexao.commit()
        print("Série cadastradod com sucesso!")

    except sqlite3.Error as e:
        print("Erro técnico:", e)
    finally:
        if conexao:
            conexao.close()

cadastrar_serie_seguro()
#SE A CONEXÃO FALHAR, ELA NÃO EXISTE EO 'FINALLY' TENTA FECHAR ALGO QUE NÃO FOI CRIADO