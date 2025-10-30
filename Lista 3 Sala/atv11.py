numeros = []
for i in range(5):
    num = int(input())
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(maior)
print(menor)
