class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial = 0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} realizado na conta {self.numero_conta}.")
        else:
            print("valor depositado invalido")

    def sacar(self, valor):
       if valor > 0:
           if self.saldo >= valor:
               self.saldo -= valor
               print(f" Saque de R${valor:.2f} realizado na conta {self.numero_conta}.")
               return True
           else:
               print(f" Erro: Saldo insuficiente na conta {self.numero_conta}.")
               return False
       else:
           print("valor invalido")

    def verificar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo}")

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, saldo_inicial=0, limite_cheque_especial=0):
        
        super().__init__(numero_conta, saldo_inicial)
        
        self.limite_cheque_especial = limite_cheque_especial
        
        print(f" conta corrente {self.numero_conta} criada com limite de cheque especial de R$ {self.limite_cheque_especial:.2f}.")
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo + self.limite_cheque_especial >= valor:
                self.saldo -= valor
                print(f" Saque de R${valor:.2f} realizado na conta corrente {self.numero_conta}.")
                if self.saldo < 0:
                    print(f"Erro: Saldo insuficinte (incluindo cheque especial) na conta {self.numero_conta}.")
                    return True
            else:
                print(f" Erro: Saldo insuficiente na conta {self.numero_conta}.")
                return False
        else:
            print("valor invalido")

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, saldo_inicial=0, taxa_juro=0.0):
        super().__init__(numero_conta, saldo_inicial)
        self.taxa_juro = taxa_juro
        print(f"conta poupança {self.numero_conta} criado com taxa de juro {self.taxa_juro*100:.2f}%.")

    def aplicar_juros(self):
        if self.taxa_juro > 0 and self.saldo > 0:
            juros = self.saldo * self.taxa_juro
            self.saldo += juros
            print(f"juros de R${juros:.2f} aplicados na conta {self.numero_conta}. Novo saldo: R${self.saldo:.2f}")
        else:
            print(f"Juros nao aplicados na conta {self.numero_conta}. Saldo não positivo ou taxa zero")

conta_corrente = ContaCorrente("12345-6", 400, 500)

print("-"*30)

conta_corrente.verificar_saldo()

print("-"*30)

conta_corrente.depositar(200.0)

print("-"*30)

conta_corrente.verificar_saldo()

print("-"*30)

conta_corrente.sacar(500)

print("-"*30)

conta_corrente.verificar_saldo()

print("-"*30)

conta_corrente.verificar_saldo(800)

print("-"*30)

conta_corrente.verificar_saldo()

print("-"*30)

conta_poupanca = ContaPoupanca("78901-2", 500.0 , 0.05)

print("-"*30)

conta_poupanca.verificar_saldo()

print("-"*30)

conta_poupanca.depositar(300.0)

print("-"*30)

conta_poupanca.verificar_saldo()
