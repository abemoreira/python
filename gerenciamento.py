fila_de_atendimento = []

while True :
    entrada = input("Digite 'Sim' para um novo client ou 'fim' para encerrar: ")
    if entrada == "sim":
        nome = input("Digite o nome do cliente: ")
        fila_de_atendimento.append(nome)
        print("fila atual:",fila_de_atendimento)
    
    elif entrada == "fim":
        break
    else:
        print("Entrada invalida.Tente norvamente")


while fila_de_atendimento:
    call = input("Digite 'atender' para chamar o proximo cliente ou 'fim' para encerrar o atendimento ")
    if call == "atender":
        cliente = fila_de_atendimento.pop(0)
        print("Atender o cliente", cliente)
        print("Fila restante", fila_de_atendimento)
    elif call == "fim":
        break
    else:
        print("Entrada invalida.Tente norvamente")

print("Sistema de atendimento encerrado")
                                                                                