print("\n------FILTRO DE PREÇOS------   ")

precos = [15, 30, 45, 60, 75]

print("Lista dos preços: ", precos)

for preco in precos:
    if preco < 50:
        print(f"Preço menor que R$50: {preco}")