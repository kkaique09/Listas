# 7) Inversão de Matriz
A = []
for i in range(10):
    try:
        A.append(float(input(f"A[{i+1}]: ")))
    except ValueError:
        A.append(0.0)

B = A[::-1]

print("Matriz B (Invertida):", B)
