import datetime

# Classe para gerenciar o sistema de pagamento
class SistemaDePagamento:
    def __init__(self, filme, horario, poltrona, preco):
        self.filme = filme
        self.horario = horario
        self.poltrona = poltrona
        self.preco = preco
        self.pago = False

    def realizar_pagamento(self):
        print(f"\nVocê escolheu o filme '{self.filme}' no horário {self.horario} e a poltrona {self.poltrona}.")
        print(f"O preço do ingresso é R${self.preco:.2f}")
        
        # Pergunta se o pagamento será feito com cartão ou dinheiro
        while True:
            print("-"*50)
            try:
                print("\nEscolha o método de pagamento:")
                print("1. Cartão")
                print("2. Dinheiro")
                print("3. Pix")
                print("-"*50)

                metodo_pagamento = input("Digite o número do método de pagamento: ")

                if metodo_pagamento == "1":  # Cartão
                    numero_cartao = input("Digite o número do cartão: ")
                    validade = input("Digite a validade do cartão (MM/AA): ")
                    cvv = input("Digite o CVV do cartão: ")
                    print("Processando pagamento com cartão...")
                    # Simulação de pagamento
                    self.pago = True
                    print("Pagamento aprovado com sucesso!")
                    break
                elif metodo_pagamento == "2":  # Dinheiro
                    valor_pago = float(input("Digite o valor em dinheiro: R$"))
                    if valor_pago >= self.preco:
                        troco = valor_pago - self.preco
                        self.pago = True
                        print(f"Pagamento aprovado! Seu troco é R${troco:.2f}")
                        break
                    else:
                        print("Valor insuficiente. Pagamento não aprovado.")
                        break
                elif metodo_pagamento == "3":  # Pix
                    chave_pix = input("Digite sua chave Pix: ")
                    print("Processando pagamento via Pix...") # Simulação de pagamento
                    self.pago = True
                    print("Pagamento aprovado com sucesso!")
                    break
                
            except ValueError:
                print("Erro de digitação. Por favor, insira um valor válido.")

    def status_pagamento(self):
        if self.pago:
            print(f"\nPagamento para o filme '{self.filme}' realizado com sucesso!")
        else:
            print(f"\nPagamento para o filme '{self.filme}' não realizado.")

# Função para verificar a idade do usuário
def verificar_idade():
    while True:
        print("-"*50)
        try:
            idade = int(input("Informe a sua idade: "))
            if idade < 18:
                print("Entrada não permitida para menores de 18 anos. Venha com um responsavel")
                return False  # Encerra a função
            elif idade >= 60:
                print("Você tem preferência no atendimento")
                return True
            else:
                print("Idade verificada. Bem-vindo!")
                return True
        except ValueError:
            print("Erro de digitação. Por favor, insira um número válido para a idade.")
     

# Função para escolher o filme, horário e poltrona
def escolher_filme_horario_poltrona(filmes):
    while True:
        print("-"*50)
        try:
            # Exibe filmes disponíveis com números para escolha
            print("\nFilmes em cartaz hoje:")
            for cont, filme in enumerate(filmes, 1):
                print(f"{cont}. {filme}:")
                for horario in filmes[filme]["horarios"]:
                    print(f"  - {horario}")

            filme_escolhido_num = input("\nEscolha um número de filme (1 a 8): ")
            try:
                filme_escolhido_num = int(filme_escolhido_num)  # Tenta converter para inteiro
                if filme_escolhido_num < 1 or filme_escolhido_num > len(filmes):
                    print("Número de filme inválido. Tente novamente.")
                    continue
            except ValueError:
                print("Escolha inválida. Digite um número correspondente ao filme.")
                continue

            filme_escolhido = list(filmes.keys())[filme_escolhido_num - 1]  # Acha o nome do filme baseado no número

            # Exibe horários disponíveis para o filme escolhido
            print("-"*50)
            print("\nHorários disponíveis:")
            for horario in filmes[filme_escolhido]["horarios"]:
                print(f"  - {horario}")

            horario_escolhido = input("\nEscolha um horário: ")
            while horario_escolhido not in filmes[filme_escolhido]["horarios"]:
                print("Horário inválido. Por favor, escolha um horário disponível.")
                horario_escolhido = input("\nEscolha um horário: ")

            # Exibe poltronas disponíveis para o horário escolhido
            print("\nPoltronas disponíveis:")
            for poltrona in filmes[filme_escolhido]["poltronas"]:
                print(f"  - {poltrona}")

            poltrona_escolhida = input("\nEscolha uma poltrona: ").upper()
            while poltrona_escolhida not in filmes[filme_escolhido]["poltronas"]:
                print("Poltrona inválida ou já ocupada. Por favor, escolha uma poltrona disponível.")
                poltrona_escolhida = input("\nEscolha uma poltrona: ").upper()

            # Marca a poltrona como ocupada
            filmes[filme_escolhido]["poltronas"].remove(poltrona_escolhida)

            return filme_escolhido, horario_escolhido, poltrona_escolhida
        except ValueError:
            print("Erro de digitação. Por favor, insira valores válidos para as escolhas.")

# Função para iniciar o atendimento
def iniciar_atendimento():
    print("-"*50)
    # Lista de filmes, horários e poltronas (Adicionando filmes do primeiro código aqui)
    filmes = {
        "Karate Kid Lendas": {
            "horarios": ["14:00", "17:20", "20:00"],
            "poltronas": ["A1", "A2", "A3", "A4", "A5"],
            "preco": 20.00
        },
        "Thunderbolts": {
            "horarios": ["13:00", "16:45", "19:30"],
            "poltronas": ["B1", "B2", "B3", "B4", "B5"],
            "preco": 25.00
        },
        "Minecraft": {
            "horarios": ["15:50", "17:10", "19:35"],
            "poltronas": ["C1", "C2", "C3", "C4", "C5"],
            "preco": 22.00
        },
        "Pecadores": {
            "horarios": ["16:30", "20:30", "21:30"],
            "poltronas": ["D1", "D2", "D3", "D4", "D5"],
            "preco": 18.00
        },
        "Until Dawn: Noite de Terror": {
            "horarios": ["19:40", "21:20", "22:05"],
            "poltronas": ["E1", "E2", "E3", "E4", "E5"],
            "preco": 26.00
        },
        "O Rei Dos Reis": {
            "horarios": ["14:05", "15:00", "16:15"],
            "poltronas": ["F1", "F2", "F3", "F4", "F5"],
            "preco": 19.00
        },
        "Homem com H": {
            "horarios": ["17:00", "20:00", "22:00"],
            "poltronas": ["G1", "G2", "G3", "G4", "G5"],
            "preco": 21.00
        },
        "A Mulher no jardim": {
            "horarios": ["15:30", "17:30", "21:45"],
            "poltronas": ["H1", "H2", "H3", "H4", "H5"],
            "preco": 23.00
        }
    }
    print("-"*50)

    # Bem-vindo ao cinema
    print("Bem-vindo ao nosso cinema!")

    # Solicita o início do atendimento
    while True:
        print("-"*50)
        try:
            resposta = input("Digite 'sim' para iniciar o atendimento ou 'não' para encerrar: ").lower()

            if resposta == 'sim':
                # Verifica a idade do usuário
                pode_entrar = verificar_idade()
                if not pode_entrar:
                    break  # Encerrar caso o usuário não tenha idade permitida

                # Escolher filme, horário e poltrona
                filme_escolhido, horario_escolhido, poltrona_escolhida = escolher_filme_horario_poltrona(filmes)

                if filme_escolhido is None:
                    break  # Caso o usuário não consiga fazer uma escolha válida

                # Criar o objeto de pagamento
                pagamento = SistemaDePagamento(filme_escolhido, horario_escolhido, poltrona_escolhida, filmes[filme_escolhido]["preco"])

                # Realiza o pagamento
                pagamento.realizar_pagamento()

                # Verifica o status do pagamento
                pagamento.status_pagamento()
                
                print("-"*50)

                break  # Sai do loop quando o atendimento é concluído
            elif resposta == 'não':
                print("Atendimento encerrado.")
                break
            else:
                print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
        except ValueError:
            print("Erro de digitação. Por favor, insira uma resposta válida.")

# Chama a função para iniciar o atendimento
iniciar_atendimento()


