get_name = input("qual é o seu nome?")
print (f"seja bem vindo, {get_name}")

get_age = input("qual sua idade ?")
age = int (get_age) 
print(f"voce tem {age} anos")

if age >= 18:
    print("voce é maior de idade")
else:
    print("voce é manor de idade")