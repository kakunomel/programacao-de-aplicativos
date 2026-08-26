def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade >= 12 and idade < 18:
        return "Adolescente"
    else:
        return "Adulto"


assert classificar_idade(10) == "Criança"
assert classificar_idade(15) == "Adolescente"
assert classificar_idade(20) == "Adulto"

print("Todos os testes passaram!")

#O erro estava no elif. 
#Pq não podemos escrever idade >= 12 and < 18. 
#A correção foi usar idade >= 12 and idade < 18, que verifica se a idade está entre 12 e 17 anos.