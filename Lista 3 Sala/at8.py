a = 1
b = 1
print(a)
print(b)
for _ in range(13):
    proximo = a + b
    print(proximo)
    a = b
    b = proximo
