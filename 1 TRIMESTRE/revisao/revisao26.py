print("------SUBSTITUIÇÃO DE DADOS------")

nomes = ["Melissa", "Kalise", "Alexandre", "Milena"]
print("Lista de nomes:", nomes)

antigo = input("\nDigite o nome que deseja mudar: ")
novo = input("Digite o novo nome: ")

posicao = 0 

while posicao < len(nomes):
    if nomes[posicao] == antigo:
        nomes[posicao] = novo 

    posicao = posicao + 1 
print("Lista atualizada:", nomes)