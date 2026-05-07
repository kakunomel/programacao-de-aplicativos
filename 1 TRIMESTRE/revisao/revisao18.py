print("------O MAIOR NÚMERO------")

valores = [12, 17, 41, 48]
maior_valor = valores[0]

for valor in valores:
    if valor > maior_valor:
        maior_valor = valor
print(f"O maior número é: {maior_valor}") 