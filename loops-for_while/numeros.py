
#n1 = float(input("Informe o primeiro número: "))
#n2 = float(input("Informe o segundo número: "))
#n3 = float(input("Informe o terceiro número: "))
#..... 
# muitas palavras
#soma = n1 + n2 + n3...
#print(f"A soma dos números é {soma}.")


soma = 0

for contador in range(5):
    numero = float(input("Informe o número: "))
    soma = soma + numero

print(f"A soma é {soma}.")

# In Python, the range() function generates a sequence of numbers,
# typically used in loops for iteration.
# By default, it creates numbers starting from 0 up to but not including a specified stop value. 