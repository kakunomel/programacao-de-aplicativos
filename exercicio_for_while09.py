ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]

item = input("Digite o nome da ferramenta que está procurando: ")

for ferramenta in ferramentas:
    if ferramenta == item:
        indice = ferramentas.index(item)
        print(f"Ferramenta encontrada! Ela está na posição {indice}")

if item not in ferramentas:

    controle = input("Deseja adicionar a ferramenta a lista?: ")

    while controle != "sair":
        ferramenta = input("Digite a ferramenta que deseja adicionar: ")
        ferramentas.append(ferramenta)
        controle = input("Deseja adicionar a ferramenta a lista?: ")
print(ferramentas)