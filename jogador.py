class Jogador:
    def __init__(self, nome, sala_atual):
        self.nome = nome
        self.sala_atual = sala_atual
        self.inventario = []

    def mover(self, direcao):
        if direcao in self.sala_atual.conexoes:
            self.sala_atual = self.sala_atual.conexoes[direcao]
            print("Você foi para o(a)", self.sala_atual.nome)
            self.sala_atual.exibir_descricao()
        else:
            print("Você não pode ir por aí.")

    def pegar_item(self, nome_item):
        for item in self.sala_atual.itens:
            if item.nome.lower() == nome_item.lower():
                self.sala_atual.remover_item(item)
                self.inventario.append(item)
                print("Você pegou:", item.nome)
                return
        print("Esse item não está aqui.")

    def exibir_inventario(self):
        print("SEU INVENTÁRIO")
        if len(self.inventario) == 0:
            print("Inventário vazio.")
        else:
            for item in self.inventario:
                print(item.nome, ":", item.descricao)