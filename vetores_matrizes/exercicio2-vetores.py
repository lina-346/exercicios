
#2

soma_dos_impares = 0

lista = [ ]

print(lista)

for i in range(10):
    entrada = int(input(f"Informe o número {i+1}: "))
    lista.append(entrada)
    if entrada % 2 != 0:
        soma_dos_impares = soma_dos_impares + entrada

print(lista)
print(soma_dos_impares)


#
# alternativa:
#

#lista = []

#for i in range(10):
#  entrada = int(input("Informe o número: "))
#  lista.append(entrada)

#somaImpares = 0
#for i in lista:
#   if i % 2 != 0:
#      somaImpares += i
#print(f"A soma dos números ímpares é {somaImpares}.")