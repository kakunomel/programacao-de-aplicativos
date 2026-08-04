import sqlite3

def cadastrar_listar_alunos():
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 1)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor

    #O COMANDO EXECUTEMANY QUEBRA COM A MENSAGEM: "FUNCTION TAKES EXACTLY 2 ARGUMENTS".
    #COMO PASSAR A LISTA DE DADOS DA FORMA CORRETA DENTRO DELE?
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", lista)

    conexao.commit()
    conexao.close()