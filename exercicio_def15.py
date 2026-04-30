print("\n------FORMATADOR DE ENDEREÇOS------")

rua = input("\nDigite o nome da sua rua: ")
numero = int(input("Digite o número da sua casa: "))
bairro = input("Digite o seu bairro: ")
cidade = input("Diite a sua cidade: ")
cep = input("Digite o seu CEP: ")

def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"RUA:{rua}, NÚMERO:{numero}, BAIRRO:{bairro}, CIDADE:{cidade}, CEP:{cep}"

informacoes = gerar_etiqueta(rua, numero, bairro, cidade, cep)
print(informacoes)
