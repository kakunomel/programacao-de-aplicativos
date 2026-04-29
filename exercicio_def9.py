print("\n------SOMADOR DE CARRINHO------")

lista_valor_compra = [89.00, 149.50, 239.00, 310.90, 8.50, 4.00, 7.00]
soma = 0

for preco in lista_valor_compra:
    soma += preco
print(f"O valor da sua compra ficou: {soma}")


def somar_carrinho (lista_valor_compra):
    if soma > 500.00:
        desconto1 = (soma * 10) / 100
        desconto2 = soma - desconto1
        return desconto2

total = somar_carrinho(lista_valor_compra)
print("Seu valor com descoonto ficou:" , total)