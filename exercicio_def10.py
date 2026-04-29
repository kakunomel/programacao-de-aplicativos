print("\n------VERIFICADOR DE PARIDADE------")

numero = int(input("Digite um número: "))

def eh_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

par_impar = eh_par(numero)
print("Seu número é", par_impar)