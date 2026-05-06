valor_da_compra = float(input("Digite o valor total da compra:"))
cupom = input("Digite o cupom:")

if cupom == "DEV10":
    desconto = valor_da_compra * 0.10
    total = valor_da_compra - desconto 
    print ("Novo valor:" , total)
else: 
    print ("Cupom inválido. Valor original: R$ " , valor_da_compra)