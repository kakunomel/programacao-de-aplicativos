print("--- INSPETOR DE QUALIDADE ---")

comprimento = input("O comprimento da peça está entre 10cm e 12 cm? Digite S ou N: ")

if comprimento == "S":
    largura = input("A largura da peça está entre 5cm e 6cm? Digite S ou N: ")
    if largura == "S":
        print("PEÇA APROVADA.")
    else:
        print("REPROVADO: Problema na largura.")
else:
    print("REPROVADO: Problema no comprimento.")

