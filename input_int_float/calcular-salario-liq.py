# Calcular o salário líquido

valor_hr_aula = float(input("Informe o valor da hora aula: R$"))
hr_trabalhadas = float(input("Informe a quantidade de horas trabalhadas por mês: "))

desc_inss = float(input("Informe a porcentagem do desconto do INSS: "))

salario_bruto = (valor_hr_aula * hr_trabalhadas)
salario_liq = (salario_bruto) - ((desc_inss / 100) * salario_bruto)

print(f"O valor do salário líquido é de R${salario_liq}")