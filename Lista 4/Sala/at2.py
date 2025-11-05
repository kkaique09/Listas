# 2) Fatorial dos Elementos
import math

def calcular_fatorial(n):
    if n < 0:
        return "Inválido"
    return math.factorial(int(n))

A = []
for i in range(6):
    try:
        A.append(int(input(f"A[{i+1}]: ")))
    except ValueError:
        A.append(0)

B = []
for elemento_a in A:
    B.append(calcular_fatorial(elemento_a))

print("Matriz B (Fatorial de A):", B)
