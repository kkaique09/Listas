nota = float(input("Digite a nota: "))
resto = nota % 1 

if resto > 0.5:
    nota_arredondada = int(nota) + 1
else:
    nota_arredondada = int(nota)

print(f"Nota arredondada: {nota_arredondada:.1f}")
