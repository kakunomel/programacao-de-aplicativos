import sqlite3

def verficar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    dados = cursor.fetchall()
    
    #PORQUE O SEGUNDO PRINT NÃO MOSTRA ABSOLUTAMENTE NADA NO CONSOLE?
    print("Primeiro print:", cursor.fetchall())
    print("Segundo print:", cursor.fetchall())
    conexao.close()
    #O FETCHALL() SÓ CONSEGUE PEGAR OS DADOS UMA ÚNICA VEZ, ENTÃO O SEGUNDO PRINT NÃO MOSTRA NADA.