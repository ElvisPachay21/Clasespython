a = 0
b = 1
contador = 0
print(a)
contador +=1

while contador < 5:
    print(b)
    a, b = b, a + b
    contador += 1
