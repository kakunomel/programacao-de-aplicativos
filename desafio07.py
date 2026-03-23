usuario1 = input("Digite o nome de um pesquisador ")

nome =["Alice", "Bob", "Carlos"]

if usuario1 in nome:
    indice = usuario1.index()
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")

usuario2 = ("Deseja remover esse pesquisador da lista (Sim/Não): ")

if usuario2 == "Sim":
    remover = usuario1.pop()
    
