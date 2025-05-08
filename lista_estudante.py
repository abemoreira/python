estudante = ["Artur", "Abe", "Antonio", "Hugo"]

print(estudante)

for nome in estudante:
    print(f"O nome dos estudante são: {nome}")

print("-" *30)

print(f" o nome do tercioro estudante é: {estudante[2]}")
print("-"*30)

#tupla
Joelma = ("joema", 35, 1.75)
print(Joelma)
print("-"*30)

#set
set1 = ("João", "john", "Hugo")

print(set1)

try:
    numero2 = int(input("insira um numero: "))

    divi = 10/ numero2

    print(divi)

except ValueError:
    print("insira um valor dado (numero)")

except ValueError:
    print("Opa! Você inciriu 0. Não se pode dividir por 0.")

print("-"*30) 

#dicionario
carro = {
    "cor": "Azul",
    "Marca": "camaro",
    "Valor": 3.0000,
    "Fabrica" : "Chevrolet"
}

print(f"a marca é {carro["Marca"]}")