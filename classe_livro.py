class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def Detalhes(self):
        print(f"Títulos: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f" Páginas:{self.autor}")

    def eh_longo(self):
        return self.paginas > 300
    
livro1 = Livro("O senhor dos aneis", "J.R.R Tolkien", 1200)
livro2 = Livro("Crepusculo", "Stephany Meyer", 100)

livro1.Detalhes()
print(f"O livro 1 é longo? {livro1.eh_longo()}")

print("-"*30)

livro2.Detalhes()
print(f" O livro 2 é longo? {livro2.eh_longo()} ")

        