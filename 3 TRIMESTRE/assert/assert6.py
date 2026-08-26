def situacao_faltas(faltas):
    if faltas <= 4:
        return "Regular"
    elif faltas >= 5 and faltas <= 10:
        return "Atenção"
    elif faltas >= 11:
        return "Reprovado por falta" 
        

assert situacao_faltas(2) == "Regular"
assert situacao_faltas(4) == "Regular"
assert situacao_faltas(6) == "Atenção"
assert situacao_faltas(8) == "Atenção"
assert situacao_faltas(12) == "Reprovado por falta" 

print("Todos os restes passaram!")