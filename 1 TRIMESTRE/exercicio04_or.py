valor_compra = float(input("Digite o valor da compra:"))
cliente = input("Digite se é cliente Prime S/N:")

if valor_compra>= 500.00 or (cliente == "S" and valor_compra >= 100.00):
    print("Parabéns! Você ganhou frete grátis")
    print("O valor da compra ficou:" , valor_compra)

frete = 50.00
valor_total = valor_compra + frete
if cliente == "N" or valor_compra < 500.00:
    print("O valor total da compra ficou:" ,  valor_total)

