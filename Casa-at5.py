massa = float(input("Digite a massa da pessoa (em kg): "))
altura = float(input("Digite a altura da pessoa (em metros): "))

imc = massa / (altura ** 2)

print(f"O IMC da pessoa é: {imc:.2f}")
