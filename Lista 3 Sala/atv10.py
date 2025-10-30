somatorio = 0
for numero in range(1, 501):
    if numero % 2 == 0:
        somatorio += numero
print(f"O somatório dos valores pares é {somatorio}")
