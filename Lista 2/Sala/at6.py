import math
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
delta = B**2 - 4*A*C
if delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)
    print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")

