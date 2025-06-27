matriz = []
print("Informe a opção desejada:\n")
while True:
    while True:
        try:   # lidando com input inválido - apesar dessa não ser a melhor maneira de se fazer isso
            op = int(input("1- Cadastro\n2- Listar\n9- Sair\n\nDigite apenas o número: "))
            match op:
                case 1:
                    print("Cadastro")
                    nome = input("Informe o nome: ")
                    nota1 = float(input("Informe a nota 1: "))
                    nota2 = float(input("Informe a nota 2: "))
                    matriz.append([nome, nota1, nota2])
                case 2:
                    print("Listagem:")
                    for aluno in matriz: 
                        media = ((aluno[1] + aluno[2]) / 2)
                        situacao = ""
                        if media >= 7:
                            situacao = "Aprovado."
                        else:
                            situacao = "Reprovado."

                        print(f"""{aluno[0]}: {aluno[1]} - {aluno[2]}.
                              Média: {media}. {situacao}""")
                case 9:
                    print("Obrigado por utilizar nosso serviços")
                    break
                case _:
                    print("Opção inválida.")
        
        except ValueError:
            print("Por favor, digite apenas um número.")
    break

