# Calcular qntd de litros que é gasta em uma viagem
# automóvel percorre 12Km/L

tempo = float(input("Informe o tempo gasto na viagem em horas: "))
velocidadeMedia = float(input("Informe a velocidade média do veículo em Km/h: "))
distancia = tempo * velocidadeMedia

litros_usados = distancia / 12

print("""
    Dados de sua viagem:
""")

print(f"""
    Velocidade média: {velocidadeMedia}Km/h
    Tempo gasto na viagem: {tempo}h
    Distância percorrida: {distancia}Km
    Quantidade de litros usada: {litros_usados:.3f}L
""")



# print("""
#    First paragraph \n\n
#    Second paragraph \n\n
#    ...
#    Last paragraph.
# """)