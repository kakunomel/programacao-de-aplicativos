import sqlite3

#O ALUNO CRIOU A CONEXÃO FORA DAS FUNÇÕES PARA "FACILITAR".
#POR QUE ISSO QUEBRA O SISTEMA QUANDO USAMOS MÚLTIPLOS ARQUIVOS(MÓDULOS)?
def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas (nomes) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()
    
#A CONEXÃO DEVE SER CRIADA DENTRO DO 'DEF' PARA EVITAR PROBLEMAS EM PROJETOS COM VÁRIOS MÓDULOS