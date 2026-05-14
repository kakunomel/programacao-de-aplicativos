print("------MEUS HÁBITOS------")

usuario = ""

def criar_arquivo():
    open('habitos.txt','w').close()


def adicionar_habitos():
    adicionar_habito = input("\nDigite o hábito que deseja adicionar: ")
    
    with open('habitos.txt','a') as arquivo:
        arquivo.write(adicionar_habito + '\n')
    print("\nHábito Cadastrado!")



def ver_habitos():
    with open('habitos.txt','r') as arquivo:
        habitos = arquivo.readlines()

        i = 0
        for habito in habitos:
            print(f"{i} - {habito.strip()}")
            i += 1



def editar_habitos():
    ver_habitos()
    posicao = int(input("Digite a posição do hábito que deseja mudar: "))
    novo_habito = input("Digite o novo hábito: ")

    with open('habitos.txt','r') as arquivo:
        linhas = arquivo.readlines()

    linhas[posicao] = novo_habito + '\n'

    with open('habitos.txt','w') as arquivo:
         arquivo.writelines(linhas)
    print("Hábito Atualizado!")



def excluir_habito():
    ver_habitos()
    posicao = int(input("Digite a posição do hábito que deseja excluir: "))

    with open('habitos.txt','r') as arquivo:
        linhas = arquivo.readlines()

    del linhas [posicao]

    with open('habitos.txt','w') as arquivo:
        arquivo.writelines(linhas)
    print("Hábito Excluido!")



while usuario != 5:

    print("\n1 - ADICIONAR HÁBITO")
    print("2 - VER HABITOS")
    print("3 - EDITAR HÁBITOS")
    print("4 - EXCLUIR HÁBITOS")
    print("5 - SAIR")

    usuario = int(input("\nDigite a opção que deseja: "))

    if usuario == 1:
        adicionar_habitos()

    elif usuario == 2:
        ver_habitos()

    elif usuario == 3:
        editar_habitos()

    elif usuario == 4:
        excluir_habito()
print("\nEcerrando programa...")