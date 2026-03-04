saldo = 1000.00
menu = int(input("Escolha 1 para Depósito, 2 para Saque e 3 para Extrato: "))

if menu == 1:
    valor = float(input("Digite o seu valor: "))
    if valor > 0.00:
        total = valor + saldo
        print("O valor depositado foi" , total)

elif menu == 2: 
    valor = float(input("Digite o valor desejado: "))
    if valor > 0 and (valor <= saldo or valor == 100.00):
        print("O valor sacado foi" , valor)

elif menu == 3:
    print("Seu saldo atual é" , saldo)