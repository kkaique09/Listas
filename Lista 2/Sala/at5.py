A = float(input("Valor A: "))
B = float(input("Valor B: "))
C = float(input("Valor C: "))
if A > B:
    A, B = B, A
if B > C:
    B, C = C, B
if A > B:
    A, B = B, A
print(A, B, C)
