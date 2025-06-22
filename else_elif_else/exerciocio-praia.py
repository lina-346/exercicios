
contador_praias_15km = 0 # sempre iniciar a variável!
qtd_praias_nao_asfaltadas = 0
qtd_veranistas_pna = 0
# Descobrir qntd de praias
num_praias = int(input("Informe o número de praias: "))
media_veranistas_pna = 0

# Receber info sobre as praias
for i in range(1, num_praias+1):
    nome_praia = input(f"Qual o nome da {i}a praia?: ")
    distancia_centro = float(input(f"Qua a distância do centro da {i}a praia? (em Km): "))
    numero_medio = int(input(f"Qual o número médio de veranistas durante a última temporada na {i}a praia?: "))
    tipo_acesso = int(input(f"Qual o tipo de acesso da {i}a praia?: (0 - Não asfaltado / 1 - Asfaltado) "))

    # numero de praias +15km do centro
    if distancia_centro > 15:
        contador_praias_15km = contador_praias_15km + 1
    
    # calcular qntd media de veranistas das praias nao asfaltadas
    if tipo_acesso == 0:
        qtd_praias_nao_asfaltadas = qtd_praias_nao_asfaltadas + 1
        qtd_veranistas_pna = qtd_veranistas_pna + numero_medio
    
    if tipo_acesso == 1 and numero_medio < 1000:
        print(f"Praias com acesso asfaltado e menos de 1000 veranistas: ")

        print(f"Praia: {nome_praia}. Distância do centro: {distancia_centro}km.")

# calcular qtd media de veranistas das praias não asfaltadas
if qtd_praias_nao_asfaltadas > 0:
    media_veranistas_pna = qtd_veranistas_pna / qtd_praias_nao_asfaltadas

print(f'Media Veranistas: {media_veranistas_pna}')
print(f'Contador a mais de 15Km do centro: {contador_praias_15km}')

