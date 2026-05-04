escolha_usuario = 1

match escolha_usuario:
    case 0:
        status = "sair do programa"
    case 1:
        status = "Entrar no programa"
    case _:
        status = "erro"

print(status)