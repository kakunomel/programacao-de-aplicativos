import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    try:
        cursor.execute("INSERT INTO turmas (nome_turma,id_serie,id_professor) VALUES (?,?,?)", (nome , id_serie , id_prof))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Professor ou série não existe.")
    finally:
        conexao.close()

#PODE DAR ERRO PORQUE NÃO EXISTE O ID_PROF, ENÃO COLOCAMOS OS TRY, EXCEPT JUNTO COM O ERRO
#SE ACONTECER O ERRO TANTO O COMMIT TANTO O CLOSE NÃO É EXECUTADO