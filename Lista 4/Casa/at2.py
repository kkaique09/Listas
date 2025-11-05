while True:
    ra_inicial = input("Digite o RA inicial (9 dígitos): ")
    if len(ra_inicial) == 9 and ra_inicial.isdigit():
        break
    print("Entrada inválida. Por favor, digite exatamente 9 dígitos numéricos.")

parte_fixa = ra_inicial[0:5] 
parte_inverter = ra_inicial[5:9] 
parte_invertida = parte_inverter[::-1]

ra_novo = parte_fixa + parte_invertida

print("\n--- Resultado da Inversão do RA ---")
print(f"RA Inicial: {ra_inicial}")
print(f"RA Novo:    {ra_novo}")
