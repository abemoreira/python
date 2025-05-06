numeros1 = (1, 2, 3)
numeros2 = (4, 5, 6)

todos_os_numeros = numeros1 + numeros2

print(f"Resultado das tuplas concatenadas: {todos_os_numeros}")

contar = numeros1.count(2)
print(f"o numero dois é repedido: {contar}")
print("-"*30)

frutas = ("banana", "maçã", "laranja", "banana")

contar = frutas.count("banana")
print(f"a fruta banana é repedida: {contar}")