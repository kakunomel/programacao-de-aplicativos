def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 25) == 150
assert calcular_desconto(50, 20) == 40

print("Todos os testes passaram!")