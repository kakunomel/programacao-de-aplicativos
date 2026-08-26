def eh_par(numero):
    return numero % 2 == 0

assert eh_par(4) == True, "Erro..."
assert eh_par(5) == False, "Erro..."
assert eh_par(0) == True, "Erro..."
assert eh_par(-3) == False, "Erro..."
print("Todos os testes passaram!")