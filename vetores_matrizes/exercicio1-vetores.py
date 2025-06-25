
#1

vetorA = []
vetorB = []

for i in range(10):
    entrada = int(input(f"Informe o {i + 1}o número: "))
    vetorA.append(entrada)

print(vetorA) # só pra conferir se foi certinho

for x in vetorA:
    if x % 2 != 0: #ímpar
        vetorB.append(x + 5)
    else:
        vetorB.append(x * 10)

print(vetorB)