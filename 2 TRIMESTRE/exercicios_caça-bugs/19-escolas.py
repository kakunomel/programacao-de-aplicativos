import sqlite3

def cadastrar_escola_manual():
    #O ALUNO RESOLVEU GERAR O ID POR CONTA PRÓPRIA
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #SE RODAR DUAS VEZES COM O ID 1, O PROGRAMA FECHA ABRUPTAMENTE (CRASH).
    #APLIQUE A BLINDAGEM PROTETORA NECESSÁRIA:
    cursor.execute("INSERT INTO escolas (id, nome) VALUES (?,?)", (id_escola, nome))

    conexao.commit()
    conexao.close()