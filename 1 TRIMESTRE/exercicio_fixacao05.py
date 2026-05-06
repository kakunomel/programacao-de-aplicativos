usuarios = ["admin", "convidado", "suporte", "teste"]
print(f"Lista de usuários: {usuarios}")

usuarios.remove("teste")
del usuarios[0]
print(f"Lista dde usuários atualizada: {usuarios}")