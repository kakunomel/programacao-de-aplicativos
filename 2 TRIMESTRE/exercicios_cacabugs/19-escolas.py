import sqlite3

def cadastrar_escola_manual():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome_escola = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO escolas (id, nome_escola) VALUES (?,?)", (id_escola, nome_escola))
        conexao.commit()
        print("Escola cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: este ID de escola já está cadastrado!")

    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)

    finally:
        conexao.close()

cadastrar_escola_manual()