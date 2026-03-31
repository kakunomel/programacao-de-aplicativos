compras = []

while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")  
    if produto.lower() == "fim":
        break

    compras.append(produto)


print("\n----- Sua Lista de Compras -----")
for item in compras:
    print(f"- {item}")