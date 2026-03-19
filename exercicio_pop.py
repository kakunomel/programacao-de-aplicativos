texto = input("Digite um texto")
cor = input("Digite uma core")
imagem = input("Insira uma imagem")

acoes = [texto , cor , imagem]
print("Lista das seguintes acões:", acoes)

acoes.pop(2)
print(f"Lista atual:{acoes}")
