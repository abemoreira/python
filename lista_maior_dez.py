numeros = [1,4,5,6,7,0,9,13,55,88,84]
numero2=[]
print("numeros pares e maiores que 10")

for i in numeros:
    if i % 2 == 0 and i > 10:
        numero2.append(i)
print(numero2)
numeros.pop(10)
numeros.pop(9)
print(numeros)
        
    
   