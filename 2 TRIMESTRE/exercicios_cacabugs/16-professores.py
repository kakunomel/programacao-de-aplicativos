import sqlite3

def inserir_professor(nome, materia, cpf):
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        #EXISTE UM ERRO DE DIGITAÇÃO NO COMANDO SQL (INSERTO).
        #POR QUE O PROGRAMA MOSTRA "CPF JÁ CADASTRADO" EM VEZ DE AVISAR SOBRE O ERRO DE SINTAXE?
        cursor.execute("ISERTO INTO professores(nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf))
        conexao.commit()
    except sqlite3.Error:
        print("Erro: Este CPF já está cadastrado no sistema!")
    finally:
        conexao.close()