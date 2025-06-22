valor_total = int(input("Informe o valor total: R$"))
num_clientes = int(input("Informe o número de clientes: "))

conta = valor_total / num_clientes

# Sistemas legados:
print("O valor é de R${0} por cliente".format(conta))


print(f"R${conta} por cliente")
