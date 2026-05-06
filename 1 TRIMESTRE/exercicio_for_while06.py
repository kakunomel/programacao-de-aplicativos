valores = [1, 5, 8, 12, 15, 22, 7, 9, 30, 4]
pares = []
impares = []

for valor in valores:
    print(f"Na lista há os seguintes números: {valor}")

    if valor % 2 == 0:
        pares.append(valor)

    else:
        impares.append(valor)
      

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")