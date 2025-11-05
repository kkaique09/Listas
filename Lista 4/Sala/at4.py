# 4) Junção de Matrizes (A de 5 e B de 5)
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

C = A + B

print("Matriz C (Junção A + B):", C)
