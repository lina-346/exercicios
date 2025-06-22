
# Ler código do item, a quantidade pedida, depois calcular o valor do lanche
# A cada iteração , perguntar ao usuário se deseja continuar

preco = 0
preco_total = 0
hot_dog = 12
hamburger = 12
cheeseburger = 13
refri = 8


while True:
    codigo = int(input("Insira o código do produto que deseja (um por vez): "))
    qntd = int(input("Quantos? "))
    if codigo == 100:
        print(f"Cachorro-quente selecionado. R${qntd * hot_dog}.")
        preco = hot_dog  
    elif codigo == 103:
        print(f"Hambúrguer selecionado. R${qntd * hamburger}.")
        preco = hamburger  
    elif codigo == 104:
        print(f"Cheesebúrguer selecionado. R${qntd * cheeseburger}.")
        preco = cheeseburger  
    elif codigo == 105:
        print(f"Refrigerante selecionado. R${qntd * refri}.")
    else:
        print("Código inválido. Por favor, tente novamente")
        qntd = 0

    preco_total = preco_total + (preco * qntd) 

    resp = input("Algo mais? (s/n): ").lower()
    
    if resp == "n":
        break

print(f"Valor total: R${preco_total}.")