# 3) Subtração de Matrizes
A = []
for i in range(5):
    try:
        A.append(float(input(f"A[{i+1}]: ")))
    except ValueError:
        A.append(0.0)

B = []
for i in range(5):
    try:
        B.append(float(input(f"B[{i+1}]: ")))
    except ValueError:
        B.append(0.0)

C = []
for i in range(5):
    C.append(A[i] - B[i])

print("Matriz C (A - B):", C)
