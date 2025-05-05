i = 0

temperaturas = []

#adcionar uma lista vazia 

while i < 5:
    temp = float(input("insira a temperatura: "))
    add = temperaturas.append(temp)
    i= i + 1

print(temperaturas)