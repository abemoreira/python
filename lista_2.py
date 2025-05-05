tarefas = []

while True:
    resposta = input("Você quer adicionar uma tarefa (sim/sair)? ").lower()

    if resposta == "sim":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)

        print("\nLista de tarefas atualizada:\n")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
        print()

    elif resposta == "sair":
        print("\nEncerrando o programa. Aqui está a lista final:")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
        break

    else:
        print("Por favor, digite 'sim' para adicionar ou 'sair' para encerrar.\n")