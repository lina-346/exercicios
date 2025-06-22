# for i in range(4257503):
#     print(i)

soma = 0 
qntd_pessoas = 0

while True:
    idade = int(input("Informe a sua idade: "))
    soma = soma + idade
    qntd_pessoas = qntd_pessoas + 1
    resp = input("Deseja continuar? (s/n) ").lower()
    if resp == "n":
        break

media = soma / qntd_pessoas
print(f"O somatório das idades é de {soma}.")
print(f"O número de pessoas é {qntd_pessoas}.")
print(f"A média das idades é {media:.2f}.")


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# #i = i + 1