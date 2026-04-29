print("\n-----FILTRO AVANÇADOS DE CANDIDATOS------")

nota_teste = int(input("Digite sua nota: "))
anos_exp = int(input("Digite o tempo de experiência: "))
possui_certificacao = input("Possui certificado? ")

def verificar_aprovacao(nota_teste, anos_exp, possui_certificacao):
    if (nota_teste > 80 and anos_exp > 2) or (possui_certificacao == "Sim"):
        print("Contratar!")
    else:
        print("Descartar!")

verificar_aprovacao(nota_teste, anos_exp, possui_certificacao)