class Pessoa:
    def __init__(self, nome , idade ):
        self.nome = nome
        self.idade= idade

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__( nome, idade)
        self.matricula = matricula
        self.curso = curso
    
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}, tenho {self.idade} anos e sou aluno do curso de {self.curso}, matricula:{self.matricula}.")

    def estudar(self):
        print(f"o aluno {self.nome} de matricula {self.matricula} está estudando {self.curso}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou professor de {self.disciplina}.")
    
    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.disciplina}")


aluno1 = Aluno("Joelma Lima", 45,"202405", "python")
professor1 = Professor("Mateus", 25, "pyton")   

aluno1.apresentar()
professor1.apresentar()

aluno1.estudar()
professor1.dar_aula()

print(f"nome do aluno: {aluno1.nome}, matricula: {aluno1.matricula}")
print(f"o professor:{professor1.nome}, da aula na disciplina de {professor1.disciplina}")