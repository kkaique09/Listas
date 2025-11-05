while True:
    ra_inicial = input("Digite o RA inicial (9 dígitos): ")
    if len(ra_inicial) == 9 and ra_inicial.isdigit():
        break
    print("Entrada inválida. Por favor, digite exatamente 9 dígitos numéricos.")

parte_a_invertida = ra_inicial[0:2][::-1]
parte_b_fixa = ra_inicial[2:7] 
parte_c_invertida = ra_inicial[7:9][::-1]

ra_novo = parte_a_invertida + parte_b_fixa + parte_c_invertida

print("\n--- Resultado da Dupla Inversão do RA ---")
print(f"RA Inicial: {ra_inicial}")
print(f"RA Novo:    {ra_novo}")
