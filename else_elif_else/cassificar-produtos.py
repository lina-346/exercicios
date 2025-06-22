

codigo_produto = int(input("Informe o código do produto: "))

if codigo_produto == 1:
    print("Alimento não perecível.")
elif 2 <= codigo_produto <= 4:
    print("Alimento perecível.")
elif 5 <= codigo_produto <= 6:
    print("Vestuário.")
elif codigo_produto == 7:
    print("Higiene pessoal")
elif 8 <= codigo_produto <= 10:
    print("Utensílios domésticos.")
else:
    print("Código inválido.")

