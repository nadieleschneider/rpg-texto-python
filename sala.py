class Sala:
    def __init__(self, id, nome, descricao_ambiente, conexoes, itens):
        self.id = id
        self.nome = nome
        self.descricao_ambiente = descricao_ambiente
        self.conexoes = conexoes
        self.itens = itens

    def exibir_descricao(self):
        print(self.nome)
        print(self.descricao_ambiente)
        if len(self.itens) > 0:
            print("Itens no chão:")
            for item in self.itens:
                print(item.nome)
        else:
            print("Não há itens aqui.")

    def listar_saidas(self):
        print("Saídas disponíveis:", list(self.conexoes.keys()))

    # Adicione este método que estava faltando:
    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)