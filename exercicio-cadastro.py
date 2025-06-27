print("Escolha a opção desejada: \n")


while True:
    opcao = int(input("1 - Cadastro\n2 - Listar\n9 - Sair\n"))
    match opcao:
        case 1:
            print("Cadastro.")
        case 2:
            print("Listar.")
        case 9:
            print("Obrigado por utilizar nosso serviço.")
            break
        case _:
            print("Opção inválida.")


# print("Escolha a opção desejada: \n")

# opcao = int(input("1 - Cadastro\n2 - Listar\n9 - Sair"))



