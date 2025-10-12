tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))

distancia = tempo * velocidade
litros_usados = distancia / 12

print(f"Velocidade média: {velocidade:.2f} km/h")
print(f"Tempo gasto: {tempo:.2f} horas")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Litros de combustível usados: {litros_usados:.2f} litros")
