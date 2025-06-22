

nome_funcionario = input("Qual o nome do funcionário? ")

salario = float(input(f"Qual o valor do salário de {nome_funcionario}? R$"))
tempo_trab = int(input(f"Por quanto anos {nome_funcionario} tem trabalhado na empresa? "))

# É bom declarar a variável no início:
bonus = 0.0

if tempo_trab >= 5:
    bonus = 0.2 * salario
    print(f"O valor do bônus é de R${bonus:.2f}.")
else:
    bonus = 0.1 * salario
    print(f"O valor do bônus é de {bonus:.2f}.")
