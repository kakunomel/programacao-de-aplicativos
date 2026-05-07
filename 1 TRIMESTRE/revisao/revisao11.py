print("--------MAIORIDADE--------")

ano_nascimento = int(input("Nos informe seu ano de nascimento: "))
ano_atual = 2026
maioridade = ano_atual - ano_nascimento

if maioridade >= 18:
    print("Você já é maior de idade!")
else:
    print("Você não é maior de idade!") 