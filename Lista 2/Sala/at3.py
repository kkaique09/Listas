a = float(input("Número 1: "))
b = float(input("Número 2: "))
if a > b:
    print(a - b)
else:
    print(b - a)

# 4
A = float(input("Lado A: "))
B = float(input("Lado B: "))
C = float(input("Lado C: "))
if A < B + C and B < A + C and C < A + B:
    if A == B and B == C:
        print("Triângulo equilátero")
    elif A == B or A == C or B == C:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")
