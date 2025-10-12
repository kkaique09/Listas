import math

raio = float(input("Digite o valor do raio da esfera: "))

volume = (4/3) * math.pi * (raio ** 3)
area = 4 * math.pi * (raio ** 2)

print(f"Volume da esfera: {volume:.2f}")
print(f"Área da superfície da esfera: {area:.2f}")
