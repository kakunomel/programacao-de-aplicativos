import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #O PROFESSOR PEDIU PARA MUDAR O NOME DO ALUNO DE ID 3,
    #MAS O SISTEMA ALTEROU O NOME DE TODOS OS ALUNOS DO BANCO DE DADOS! CORRÇÃO URGENTE:
    cursor.execute("UPDATE alunos SET nome = ?", (novo_nome))

    conexao.commit()
    conexao.close()
    