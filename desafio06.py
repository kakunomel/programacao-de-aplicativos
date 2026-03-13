print("------PREENCHA OS SEGUINTES DADOS------")

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
telefone = int(input("Qual o seu telefone? "))
carteira = input("Possui carteira de motorista? ")

print("--------------------------------------")

if nome == "João" or "Thiago" or "Pedro" or "Matheus":
    print("")

if telefone == 99999999:
    print("Telefone inválido!")

if idade < 0 or idade > 120:
    print("Idade inválida!")

lista = [nome , idade , telefone , carteira]

print(f"Olá {nome}, descobrimos que você tem {idade} anos, rackeamos seu telefone {telefone} e será que você tem carteira? {carteira}.")