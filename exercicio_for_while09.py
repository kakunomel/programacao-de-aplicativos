ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]

item = input("Digite o nome da ferramenta que está procurando: ")

for ferramenta in ferramentas:
    if item == ferramenta:
        indice = ferramentas.index(ferramenta)
        print(f"Ferramenta encontrada! Ela está na posição {indice}")

controle = input("Deseja adicionar a ferramenta a lista?: ")

while controle != "n":
    ferramenta = input("Digite a ferramenta que deseja adicionar: ")
    ferramentas.append(ferramenta)
    controle = input("Deseja adicionar a ferramenta a lista?: ")

