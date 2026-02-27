nome_cliente = input("Digite o seu nome:")
valor_total = float(input("Digite o valor total da compra:"))
distancia_entrega = int(input("Digite a distância da entrega:"))
cupom = input("Digite o cupom:")
frete = 40.00

if valor_total >= 1000.00 and cupom == "S":
    desconto = valor_total * 0.20
    total = valor_total - desconto
    print("Parabéns! Você ganhou um Mousepad Gamer de brinde!")
elif valor_total > 500.00 and valor_total < 1000.00 and cupom == "S":
    desconto = valor_total * 0.10
    total = valor_total - desconto
    
if distancia_entrega <= 50 and valor_total > 200.00:
    frete = 0.00
    valor_final = valor_total + frete
else:
    valor_final = valor_total + frete

print("Nome do cliente:" , nome_cliente)
print("Valor total da compra:" , valor_total)
print("Valor do desconto:" , cupom)
print("Valor final a pagar:" , valor_final)