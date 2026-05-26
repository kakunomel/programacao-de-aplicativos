#É para habilitar a biblioteca nativa do Python responsável por manipular dados no formato JSON. Ela permite converter estruturas de dados Python em texto JSON e vice-versa.
import json
#Serve para verificar se o arquivo de dados já existe no computador.
import os

#Salva as informações dos alunos
BANCO_DADOS = 'alunos.json'



#É uma função para guardar os códigos para cadastrar os alunos
def cadastrar():
    #Serve para aparecer no terminal '--- Novo Cadastro---'
    print("\n--- Novo Cadastro ---")
    
    #Serve para verificar se o arquivo BANCO_DADOS existe
    if os.path.exists(BANCO_DADOS):
        #Serve para abrir o arquivo em formato de leitura
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            #Lê o arquivo
            alunos = json.load(f)
    #Cria uma lista com o nome 'alunos'
    else:
        alunos = []

    #Uma variável para cadastrar novos alunos
    novo_aluno = {
        #Chave para por os nomes
        "nome": input("Nome: "),
        #Chave para por o telefone
        "telefone": input("Telefone: "),
        #Chave para por a turma
        "turma": input("Turma: "),
        #Chave para por a idade
        "idade": int(input("Idade: ")),
        #Chave para por o CPF
        "cpf": input("CPF: ")
    }
    
    #É para adicionar um aluno novo na lista de alunos
    alunos.append(novo_aluno)

    #Serve para abrir o arquivo e escrever as informações dos alunos
    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
        #Escreve no arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False)

    #É para aparecer no terminal: "Aluno cadastrado com sucesso!"    
    print("Aluno cadastrado com sucesso!")



#É uma função para guardar os códigos para listar os alunos cadastrados
def listar():
    #É para aparecer no terminal: "--- Lista de Alunos ---"
    print("\n--- Lista de Alunos ---")
    
    #Serve para verificar se o arquivo BANCO_DADOS existe
    if os.path.exists(BANCO_DADOS):
        #Serve para abrir o arquivo em formato de leitura
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            #Lê o arquivo
            alunos = json.load(f)
    #Cria uma lista com o nome 'alunos'
    else:
        alunos = []

    if not alunos:
        #É para aparecer no terminal: "Nenhum aluno cadastrado"
        print("Nenhum aluno cadastrado.")
        #Encerra a função"
        return

    #A cada aluno que está na lista alunos:
    for aluno in alunos:
        #Aparece no terminal o nome, CPF, turma e telefone de todos os alunos da lista
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")



#É uma função para guardar os códigos para atualizar o cadastro dos alunos
def atualizar():
    #É para aparecer no terminal: "--- Atualizar Aluno---"
    print("\n--- Atualizar Aluno ---")
    #Se o arquivo BANCO_DADOS não existir:
    if not os.path.exists(BANCO_DADOS):
        #É para aparecer no terminal: "Nenhum aluno cadastrado no sistema."
        print("Nenhum aluno cadastrado no sistema.")
        #Encerra a função
        return

    #Serve para abrir o arquivo em formato de leitura
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        #Lê o arquivo
        alunos = json.load(f)

    #Uma variável para informar o CPF de um aluno que deseja editar  
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")
    
    #A cada aluno que está na lista alunos:
    for aluno in alunos:
        #Se aluno de X CPF for igual o CPF da variável cpf_busca:
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}") #Mostra na tela o nome do aluno que foi encontrado para edição.
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']  #Atualiza o nome do aluno 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] #Atualiza o telefone 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] #Atualiza a turma
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) #Atualiza a idade
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] #Atualiza o CPF
            
           #Abre o arquivo em formato de write e substitui as informações que ja estavam salvas
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                #Escreve no arquivo
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            #É para aparecer no terminal: "Dados atualizados com sucesso!"
            print("Dados atualizados com sucesso!")
            #Encerra a função
            return

    #É para aparecer no terminal: "Aluno não encontrados."  
    print("Aluno não encontrado.")



#É uma função para guardar os códigos para excluir o aluno desejado
def excluir():
    #É para aparecer no terminal: "---Excluir Aluno ---"
    print("\n--- Excluir Aluno ---")
    #Se o arquivo BANCO_DADOS não existir:
    if not os.path.exists(BANCO_DADOS):
        #É para aparecer no terminal: "Nenhum aluno cadastrado no sistema."
        print("Nenhum aluno cadastrado no sistema.")
        #Encerra a função
        return

    #Abre o arquivo em formato de leitura
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        #Lê o arquivo
        alunos = json.load(f)

    #Uma variável para informar o CPF de um aluno que deseja remover  
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]
    
    #Se a nova lista for menor que a lista de alunos:
    if len(nova_lista) < len(alunos):
        #Abre o arquivo em formato de write e substitui as informações que ja estavam salvas
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            #Escreve no arquivo
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        #Vai aparecer no terminal: "Aluno removido com sucesso!"
        print("Aluno removido com sucesso!")
    else:
        #Vai aparecer no terminal: "Aluno não encontrado"
        print("Aluno não encontrado.")



#É uma função para guardar os códigos que mostram as opções
def menu():
    #Se o arquivo BANCO_DADOS não existir:
    if not os.path.exists(BANCO_DADOS):
        #Abre o arquivo em formato de write
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            #Escreve no arquivo
            json.dump([], f)

    while True:
        #Vai aparecer no terminal como um menu: ===SISTEMA ESCOLAR===
        print("\n=== SISTEMA ESCOLAR ===")
        #Vai aparecer no terminal: "1. Cadastrar Aluno"
        print("1. Cadastrar Aluno")
        #Vai aparecer no terminal: "2. Listar Alunos"
        print("2. Listar Alunos")
        #Vai aparecer no terminal: "3. Atualizar Aluno"
        print("3. Atualizar Aluno")
        #Vai aparecer no terminal: "4. Excluir Aluno"
        print("4. Excluir Aluno")
        #Vai aparecer no terminal: "5. Sair"
        print("5. Sair")
        
        #É para poder escolher a opção que deseja
        opcao = input("Escolha uma opção: ")
        
        #Se a opção escolhida for 1, chama-se a função de cadastrar
        if opcao == '1': cadastrar()
        #Se a opção escolhida for 2, chama-se a função de listar
        elif opcao == '2': listar()
        #Se a opção escolhida for 3, chama-se a função de atualizar
        elif opcao == '3': atualizar()
        #Se a opção escolhida for 4, chama-se a função de excluir
        elif opcao == '4': excluir()
        #Se a opção escolhida for 5, o break para o código 
        elif opcao == '5': break
        #Se a opção nao for nenhum n° de 1 a 5, aparece o terminal 'Opção Inválida!'
        else: print("Opção inválida!")

#Chama a função
menu()