P1 = float(input("Digite a nota da primeira avaliação (P1): "))
P2 = float(input("Digite a nota da segunda avaliação (P2): "))
Ativ = float(input("Digite a nota das atividades (Ativ): "))

media = (P1 * 4 + P2 * 4 + Ativ * 2) / 10

print(f"A média semestral é: {media:.2f}")
