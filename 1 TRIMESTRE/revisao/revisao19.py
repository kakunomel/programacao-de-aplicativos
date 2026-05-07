print("\n------DESCONTO DE LOJA------")

valor_compra = float(input("Digite o valor total da compra: "))

if valor_compra > 100:
    conta = (valor_compra * 10) / 100
    desconto = valor_compra - conta
    print(f"\nVocê recebeu 10% de desconto!")
    print(f"O valor total da compra ficou: {desconto}")
else:
    print(f"\nO valor total da compra foi: {valor_compra}")