s0 = 2      
v0 = 3      
a = 10     

t = float(input("Digite o valor do tempo t (em segundos): "))

s = s0 + v0 * t + 0.5 * a * (t ** 2)

print(f"O valor da posição s após {t} segundos é: {s:.2f} metros")
