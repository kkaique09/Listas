# 6) Quadrado dos Elementos
A = []
for i in range(8):
    try:
        A.append(float(input(f"A[{i+1}]: ")))
    except ValueError:
        A.append(0.0)

B = []
for elemento_a in A:
    B.append(elemento_a ** 2)

print("Matriz B (A²):", B)
