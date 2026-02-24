nome_do_produto = input("Digite o produto escolhido: ")
preço_unitário = float(input("Digite o valor do produto: "))
quantidade_de_produto = int(input("Digite a quantidade de produto: "))

multiplicação = preço_unitário * quantidade_de_produto

print ("Nome do produto: " , nome_do_produto)
print ("Quantidade adquirida: " , quantidade_de_produto)
print ("Valor unitário: " , preço_unitário)
print ("Valor total a ser pago é: " , multiplicação)