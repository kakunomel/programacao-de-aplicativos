print("\n-----PLANEJADOR DE VIAGENS-----\n")

usuario = ""

def criar_arquivo():
    open('viagens.txt','w').close()
criar_arquivo()

def adicionar_destinos():
    destinos = input("\nDê uma sugestão de um lugar: ")
    with open('viagens.txt','a') as arquivo:
        arquivo.write(destinos + '\n')
    print("Destino Cadastrado!\n")


def listar_destinos():
    with open('viagens.txt','r') as arquivo:
        destinos = arquivo.readlines()
        
        i = 0
        for destino in destinos:
            print(f"\n{i} - {destino.strip()}")
            i += 1


def editar_destinos():
    listar_destinos()
    posicao = int(input("\nDigite a posição do destino que deseja alterar: "))
    novo_destino = input("Digite o novo destino: ")

    with open('viagens.txt','r') as arquivo:
        linhas = arquivo.readlines()

    linhas[posicao] = novo_destino + '\n'

    with open('viagens.txt','w') as arquivo:
        arquivo.writelines(linhas)
    print("Destino Atualizado!")


def remover_destinos():
    listar_destinos()
    posicao = int(input("\nDigite a posição do destino que deseja remover: "))

    with open('viagens.txt','r') as arquivo:
        linhas = arquivo.readlines()

    del linhas[posicao]

    with open('viagens.txt','w') as arquivo:
        arquivo.writelines(linhas)
    print("Destino Removido!") 


while usuario != 5:
    
    print("\n1 - ADICIONAR DESTINOS")
    print("2 - LISTAR DESTINOS")
    print("3 - EDITAR DESTINOS")
    print("4 - EXCLUIR DESINOS")
    print("5 - SAIR")

    usuario = int(input("\nDigite a opção que deseja: "))

    if usuario == 1:
        adicionar_destinos()

    elif usuario == 2:
        listar_destinos()

    elif usuario == 3:
        editar_destinos()

    elif usuario == 4:
        remover_destinos()
print("\nEcerrando programa...")
    
