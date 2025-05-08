class Carro:
    tipo_veiculo = "Automovel"

    def __init__(self, marca, modelo, ano):
        
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    #Metodo de instancia
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O {self.marca} {self.modelo} acelerou para{self.velocidade} km/h")

    #Metodo de intância
    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
            print(f"O {self.marca} {self.modelo} freio para{self.velocidade} km/h")
        
#colocando 
carro1 = Carro("toyota", "Corola", 2022)
carro2 = Carro("chevrolet", "S10", 2023)

#acessando os atributos
print(carro1.modelo)
print(carro2.ano)

#acessando os metodos 
carro1.acelerar(60)
carro2.frear(10)

print(f"a velocidade do carro foi {carro1.acelerar}")