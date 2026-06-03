import json
import os


MATRICULA = 'alunos.json'

def cadastrar_aluno():
    print("\n---CADASTRAR ALUNO---")

    if os.path.exists(MATRICULA):
        with open(MATRICULA, 'r', encoding='utf-8') as arquivo:
            alunos = json.load(arquivo)
    else:
        alunos = []

    id_aluno = int(input("Qual é o seu ID"))
    novo_aluno = { 
        "ID": id_aluno,
        "nome": input("Nome: "), 
        "telefone": input("Telefone: "), 
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ") 
    }          
      
    if len(alunos) !=0:
        for dados in alunos:
            if dados["ID"] == id_aluno:
                print("ID já possui cadastro! ")
                return

    alunos.append(novo_aluno)
    with open (MATRICULA, 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, f, indent=4)
    print("Aluno cadastrado! ")   


def listar_alunos():
    print("\n---LISTA DE ALUNOS---")

    
    if os.path.exists(MATRICULA):
        with open(MATRICULA, 'r', encoding='utf-8') as arquivo:
            alunos = json.load(arquivo)
    else:
        alunos = []

    if not alunos:
     print("Nenhum aluno cadastrado.")
     return
    
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") 
    

def atualizar_alunos():

    print("\n---ATUALIZAR ALUNOS---") 
    if not os.path.exists(MATRICULA):
        print("Nenhum aluno cadastrado no sistema.") 
        return

    with open(MATRICULA, 'r', encoding='utf-8') as arquivo: 
        alunos = json.load(arquivo) 
         
    id_aluno = int(input("Digite o CPF do aluno que deseja editar: ")) 

    for aluno in alunos:  
        if aluno['ID'] == id_aluno: 
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']  
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) 
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']  

            with open(MATRICULA, 'w', encoding='utf-8') as arquivo: 
                json.dump(alunos, arquivo, indent=4, ensure_ascii=False) 
            print("Dados atualizados com sucesso!") 
            return 
        
    print("Aluno não encontrado.")


def excluir():
    print("\n---EXCLUIR ALUNO---") 
    if not os.path.exists(MATRICULA): 
        print("Nenhum aluno cadastrado no sistema.") 
        return  

    with open(MATRICULA, 'r', encoding='utf-8') as arquivo: 
        alunos = json.load(arquivo) 
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] 

    if len(nova_lista) < len(alunos): 
        with open(MATRICULA, 'w', encoding='utf-8') as arquivo:  
            json.dump(nova_lista, arquivo, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")  
    else: 
        print("Aluno não encontrado.") 


def menu():  
    if not os.path.exists(MATRICULA): 
        with open(MATRICULA, 'w', encoding='utf-8') as arquivo: 
            json.dump([], arquivo)
    
    while True:  
      print("\n=== SISTEMA DE MATRÍCULA ===")  
      print("1- CADASTRAR ALUNO") 
      print("2- Listar Alunos")
      print("3- Atualizar Aluno") 
      print("4- Excluir Aluno") 
      print("5- Sair") 

      opcao = input("Escolha uma opção: ")

      if opcao == '1': cadastrar() 
      elif opcao == '2': listar() 
      elif opcao == '3': atualizar() 
      elif opcao == '4': excluir() 
      elif opcao == '5': break 
      else: print("Opção inválida!")
menu()
  

          