a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c

if a != maior and a != menor:
    meio = a
elif b != maior and b != menor:
    meio = b
else:
    meio = c

print(f"Menor número: {menor}")
print(f"Número do meio: {meio}")
print(f"Maior número: {maior}")
