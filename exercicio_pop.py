texto = input("Digite um texto ")
cor = input("Digite uma cor ")
imagem = input("Descreva uma imagem ")

acoes = [texto , cor , imagem]
print("Lista das seguintes acões:", acoes)

acoes.pop(2)
print(f"Lista atual:{acoes}")
