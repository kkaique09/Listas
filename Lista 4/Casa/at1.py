while True:
    rav = input("Digite o RA infectado (RAV - 9 dígitos): ")
    if len(rav) == 9 and rav.isdigit():
        break
    print("Entrada inválida. Por favor, digite exatamente 9 dígitos numéricos.")

rac = (
    rav[0] +
    rav[1] +
    rav[7] +
    rav[6] +
    rav[4] +
    rav[5] +
    rav[2] +
    rav[3] +
    rav[8]
)

print("\nResultado da Recomposição\n")
print(f"RAV (Infectado): {rav}")
print(f"RAC (Correto):   {rac}")
