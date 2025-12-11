pontuacoes = [5, 9, 3, 10, 2, 7, 8]

criticas_encontradas = 0

for pontos in pontuacoes:
    if pontos >= 8:
       criticas_encontradas += 1

print("Máquinas em situação crítica:", criticas_encontradas)