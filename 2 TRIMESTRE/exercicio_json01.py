#
import json
#
import os

#Salva as informações dos alunos
BANCO_DADOS = 'alunos.json'

#É uma função para guardar os códigos para cadastrar os alunos
def cadastrar():
    #Serve para aparecer no terminal '--- Novo Cadastro---'
    print("\n--- Novo Cadastro ---")
    
    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []

    novo_aluno = {
        "nome": input("Nome: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }
    
    alunos.append(novo_aluno)

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
        
    print("Aluno cadastrado com sucesso!")

#É uma função para guardar os códigos para listar os alunos cadastrados
def listar():
    print("\n--- Lista de Alunos ---")
    
    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

#É uma função para guardar os códigos para atualizar o cadastro dos alunos
def atualizar():
    print("\n--- Atualizar Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

#É uma função para guardar os códigos para excluir o aluno desejado
def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

#É uma função para guardar os códigos que mostram as opções
def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
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