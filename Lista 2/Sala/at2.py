n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
if media >= 6:
    print(f"Aprovado com média {media:.2f}")
else:
    exame = float(input("Nota do exame: "))
    nova_media = (media + exame) / 2
    if nova_media >= 5:
        print(f"Aprovado em exame com média {nova_media:.2f}")
    else:
        print(f"Reprovado com média {nova_media:.2f}")
