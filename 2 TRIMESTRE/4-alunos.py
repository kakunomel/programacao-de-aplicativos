import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    #SE O USUÁRIO DIGITAR "TURMA B" EM VEZ DO NÚMERO DO ID, O SISTEMA QUEBRA.
    #O TRY/EXCEPT ABAIXO FALHOU EM CAPTURAR ESSE ERRO. QUAL O PROBLEMA?
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola,db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("Erro no banco de dados!")
    finally:
        conexao.close()