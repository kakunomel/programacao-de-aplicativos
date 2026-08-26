def buscar_nome(lista, nome):
 	return nome in lista

assert buscar_nome(["Maria", "Melissa", "Júlia"], "Melissa") == True
assert buscar_nome([], "Melissa") == False
assert buscar_nome(["Maria", "Melissa"], "Júlia") == False


def tem_senha_valida(senha):
    return len(senha) >= 8

assert tem_senha_valida("12345678") == True
assert tem_senha_valida("") == False
assert tem_senha_valida("1234567") == False


print("Testes aprovados!")

#Ao buscar um nome em uma lista vazia,
#o resultado será False, pois nenhum nome está presente nela.