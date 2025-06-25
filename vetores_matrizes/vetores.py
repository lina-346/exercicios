
vetor = [ ]
print(vetor)

frutas = ["banana", "maçã", "pera"]
print(frutas[1])

frutas[0] = "banana da terra"
print(frutas)

vetor.append("Fulano")
frutas.append("mamão")
print(vetor)
print(frutas)

frutas.insert(1, "açaí")
print(frutas)

entrada = input("Informe o nome da fruta: ")
frutas.append(entrada)
print(frutas)