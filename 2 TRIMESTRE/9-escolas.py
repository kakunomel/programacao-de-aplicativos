import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a rmover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #ESSE COMANDO VAI APAGAR O BANCO INTEIRO SE O ALUNO NÃO PRESTAR ATENÇÃO.
    cursor.execute("DELETE FROM escolas WHERE id = id_escola")

    conexao.commit()
    conexao.close()
    