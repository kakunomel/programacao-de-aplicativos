import sqlite3

def cadastrar_listar_alunos():
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 1)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.executemany("INSERT INTO alunos (nome_aluno, id_serie) VALUES (?,?)", lista)

    conexao.commit()
    print(lista)
    conexao.close()

cadastrar_listar_alunos()