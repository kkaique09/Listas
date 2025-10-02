import math
raio = float(input("Digite o raio da lata de óleo (em cm):"))
altura = float(input("Digite a altura dalata de óleo ( em cm):"))

volume = math.pi * raio ** 2 * altura 
print("Volume dalata de óleo:", volume, "cm³")