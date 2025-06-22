
numero = int(input("Deseja ver a tabuada de que número?: "))

print(f"Tabuada do {numero}:")

for i in range(1, 11):  # "Para cada número i de 1 até 10, faça o que está dentro do bloco indentado."
    print(f"{numero} x {i} = {numero * i}")

# A função print() serve para mostrar coisas na tela — e o que ela mostra sempre é texto (ou seja, string).
# Então, tudo que você quer que apareça como frase ou explicação, precisa ser transformado em texto (string).
# Se você só mandar números ou expressões, ele imprime só o valor.
# Mas se quiser algo "explicativo" então precisa transformar isso tudo em texto — ou seja, em uma string.

# range(start, stop, step) - 3 Parameter Form