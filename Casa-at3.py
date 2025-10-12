altura_parede = float(input("Insira o valor da ALTURA da parede:\n"))
largura_parede = float(input("Insira o valor da LARGURA da parede:\n"))
area_parede = altura_parede * largura_parede
print(f"A Area da parede é: {area_parede:.2f} metros quadrados\n")
altura_azulejo = float(input("Insira o valor da ALTURA do azulejo:\n"))
largura_azulejo = float(input("Insira o valor da LARGURA do azulejo:\n"))
area_azulejo = altura_azulejo * largura_azulejo
print(f"A Area do azulejo é: {area_azulejo:.2f} metros quadrados\n")
quantidade_azulejos = area_parede / area_azulejo
print(f"A Quantidade de azulejos necessario para azulejar a parede é: {quantidade_azulejos}")
