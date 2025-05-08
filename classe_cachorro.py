class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} está latindo!")

meu_cachorro = Cachorro("Rex", 5)
outro_cachorro = Cachorro("Ben", 8)

print(f" Meu cachorro se chama {meu_cachorro.nome} e tem {meu_cachorro.idade}")

meu_cachorro.latir()   
outro_cachorro.latir()  