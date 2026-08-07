import sqlite3

def cadastrar_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    nome_serie = input("\nDigite sua série: ")
    id_serie = int(input("Digite o ID da sua serie: "))
    id_professor = int(input("Digite o ID do professor: \n"))

    try:
        cursor.execute("INSERT INTO series (nome_serie,id_serie,id_professor) VALUES (?,?,?)", (nome_serie, id_serie, id_professor))
        conexao.commit()

    except sqlite3.IntegrityError:
        print("Professor ou série não existe.")

    finally:
        conexao.close()

cadastrar_turma()