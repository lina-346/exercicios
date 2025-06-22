numero = int(input("Informe um número inteiro: "))

resultado = 1 # 1 não vai alterar o resultado final pois a operação é de multiplicação

# "Para cada número i de [numero] até 1, em ordem decrescente, faça o que está dentro do bloco indentado."
for i in range(numero, 0, -1):  
    resultado = resultado * i  # "pegar [resultado]", multiplicar ele mesmo pelo próximo n°, baseado nas instruções anteriores

#for i in range(numero, 0, -1): 
    # numero: começa com o número que o usuário colocou
    # 0: para antes de chegar no zero (ou seja, para no 1)
    # -1: o loop vai diminuindo por -1
#  range(start, stop, step) - 3 Parameter Form


print(f"O fatorial de {numero} é {resultado}.")

