# Cálculo prestação em atraso

valor = float(input("Informe o valor da prestação: R$"))
taxa = float(input("Informe a porcentagem da taxa: "))
tempo = int(input("Informe o tempo de atraso em dias: "))

prestacao = valor + ((valor * taxa/100) * tempo)

print(f"""
O valor da prestação é de R${prestacao:.2f}
""")
