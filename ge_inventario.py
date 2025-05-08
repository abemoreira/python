class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionar ao invertário.")

    def lista_itens(self):
        print("itens no inventário")
        if not self.itens:
            print("o inventario está vazio")
        else:
            for i, item in enumerate(self.itens):
                print(f"{i +1}. {item}")

meu_inventario = Inventario()

meu_inventario.adicionar_item("espada longa")
meu_inventario.adicionar_item("escudo")
meu_inventario.adicionar_item("porçao")
meu_inventario.adicionar_item("flexa(x20)")   
    
meu_inventario.lista_itens()