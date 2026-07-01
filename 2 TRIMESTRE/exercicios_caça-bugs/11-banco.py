import sqlite3

#O ALUNO CRIOU A CONEXÃO FORA DAS FUNÇÕES PARA "FACILITAR".
#POR QUE ISSO QUEBRA O SISTEMA QUANDO USAMOS MÚLTIPLOS ARQUIVOS(MÓDULOS)?
conexão = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escolas (nomes) VALUES (?)", (nome,))
    conexa.commit()
    