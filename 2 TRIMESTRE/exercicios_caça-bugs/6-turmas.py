import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    #SE O ID_PROF NAO EXISTIR, OCORRE UM INTEGRITYERROR.
    #SE O ERRO ACONTECER, O QUE OCORRE COM A LINHA CONEXAO.CLOSE()?
    cursor.execute("INSERT INTO turmas Iome_turma, id_serie, id_professor) VALUES (?, ?, ?)", (nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()
    