def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    else:
 	    return "Reprovado"

assert situacao_aluno(10) == "Aprovado"
assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(4) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"

print("Todos testes passaram!")