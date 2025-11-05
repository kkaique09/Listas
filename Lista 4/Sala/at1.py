# 1) Multiplicação por 3
A = []
for i in range(5):
    try:
        A.append(float(input(f"A[{i+1}]: ")))
    except ValueError:
        A.append(0.0)

B = []
for elemento_a in A:
    B.append(elemento_a * 3)

print("Matriz B (A * 3):", B)
