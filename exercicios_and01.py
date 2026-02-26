idade = int(input("Digite a sua idade:"))
saldo = float(input("Digite o seu saldo:"))

if idade >= 18 and saldo >= 50.0:
    print ("Acesso autorizado! Bem-vindo ao evento")
elif idade < 18 and saldo <50.0:
    print ("Infelizmente você não cumpre os requisitos de entrada.")
elif idade >= 18 and saldo < 50.0:
    print("Infelizmente você não cumpre os requisitos de entrada.")
elif idade < 18 and saldo >= 50.0:
    print("Infelizmente você não cumpre os requisitos de entrada.")
    