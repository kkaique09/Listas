valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros ( em %): "))
tempo = float(input("Digite o tempo de atraso ( em meses): "))

prestacao = valor + (valor * (taxa/100) * tempo)
print("Valor da prestação em atraso:", prestacao)
