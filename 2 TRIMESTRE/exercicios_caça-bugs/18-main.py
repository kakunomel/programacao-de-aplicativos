import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escolaa.db')
    cursor = conexao.cursor

    #O SQLITE JOGA UM ERRO DE SINTAXE OPERACIONAL INDICANDO QUE NÃO ACEITA O CARACTERE '?'.
    #NÃO PODEMOS PARAMETRIZAR NOMES DE TABELAS? COMO RESOLVER MANTENDO A SEGUANÇA?
    cursor.execute("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro))

    print(cursor.fetchone())
    conexao.close()