def classificar_temperatura(temperatura):
    if temperatura <= 15:
        return "Frio"
    elif temperatura > 15 and temperatura <= 25:
        return "Agradável"
    elif temperatura > 25:
        return "Quente"
 	
assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(15) == "Frio"
assert classificar_temperatura(20) == "Agradável"
assert classificar_temperatura(25) == "Agradável"
assert classificar_temperatura(30) == "Quente"

print("Todos os teste passaram!")