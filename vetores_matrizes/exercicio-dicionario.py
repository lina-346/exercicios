# Dicionário

matriz = []
print("Informe a opção desejada:\n")
while True:
    op = int(input("1- Cadastro\n2- Listar\n9- Sair\n\nDigite apenas o número: "))
    match op:
        case 1:
            print("Cadastro")
            aluno = {}
            aluno["nome"] = input("Nome do aluno: ")
            aluno["nota1"] = float(input("Informe a nota 1: "))
            aluno["nota2"] = float(input("Informe a nota 2: "))
            matriz.append(aluno)
        case 2:
            print("Listagem:")
            for aluno in matriz: 
                media = ((aluno["nota1"] + aluno["nota2"]) / 2)
                situacao = ""
                if media >= 7:
                    situacao = "Aprovado."
                else:
                    situacao = "Reprovado."
                print(f'{aluno["nome"]}: {aluno["nota1"]} - {aluno["nota2"]}.\nMédia: {media}. {situacao}\n')
        case 9:
            print("Obrigado por utilizar nosso serviços")
            break
        case _:
            print("Opção inválida.")