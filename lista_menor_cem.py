numeros = []
todos_validos = True

for entrada in range(5):
    entrada = float(input("insira um numero: "))
    numeros.append(entrada)

for i in numeros:
    if not (i > 0 and i < 100):
        todos_validos = False
        break

if todos_validos:
    print("todos os numeros numeros sao positivo e menores que 100")
else:
    print("nem todos os numeros sao positivos e menores que 100")