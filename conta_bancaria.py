class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        print(f" conta para {self.titular} criada com sucesso")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Saque de R${valor:.2f}")
        else:
            print("valor depositado invalido")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f" Saque de R${valor:.2f} realizado. Verique seu saldo atual: R${self.saldo:.2f}")
            else:
                print("valor de deposito invalido.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f" Saque de R${valor:.2f} realizado com sucesso. saldo atual: R${self.saldo:.2f}")
            else:
                print("saldo insuficiente para realizar o saque.")
        else:
            print("valor de saque invalido.")

    def consultar_saldo(self):
         print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")

conta_joao = ContaBancaria("João Silva")

conta_joao.depositar(1000)
conta_joao.depositar(700)
conta_joao.consultar_saldo()