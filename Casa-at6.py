import math

raio = float(input("Digite o valor do raio da circunferência: "))

area = math.pi * (raio ** 2)
comprimento = 2 * math.pi * raio

print(f"Área do círculo: {area:.2f}")
print(f"Comprimento da circunferência: {comprimento:.2f}")
