numero = 6

print("tenta acerta o numero que eu to pensando de 1 a 10")

get_numero = int(input("digite o seu palpite: "))

if get_numero == numero:
    print("Parabens.Você acertou")
elif get_numero < numero:
    print("tente novamente. O valor esta muito baixo")
elif get_numero > numero:
    print ("tente novarmente.Ovalor esta muito alto")

else :
    print("tente norvamente")