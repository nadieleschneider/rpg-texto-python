import json
from item import Item
from sala import Sala
from jogador import Jogador

with open("mapa.json", "r", encoding="utf-8") as arquivo:
    mapa_dados = json.load(arquivo)

    salas = {}
    for sala_id, sala_dados in mapa_dados.items():
        lista_itens = []
        for item_dado in sala_dados.get("itens", []):
            item_obj = Item(item_dado["id"], item_dado["nome"], item_dado["descricao"])
            lista_itens.append(item_obj)

        sala = Sala(
            id=sala_dados["id"],
            nome=sala_dados["nome"],
            descricao_ambiente=sala_dados["descricao_ambiente"],
            conexoes=sala_dados["conexoes"],
            itens=lista_itens
        )
        salas[sala.id] = sala

nome_jogador = input("Digite o nome do seu personagem: ")
jogador = Jogador(nome=nome_jogador, sala_atual=salas["saguao"])

for sala_obj in salas.values():
    conexoes_reais = {}
    for direcao, id_destino in sala_obj.conexoes.items():
        if id_destino in salas:
            conexoes_reais[direcao] = salas[id_destino]
    sala_obj.conexoes = conexoes_reais

jogador.sala_atual.exibir_descricao()
jogador.sala_atual.listar_saidas()

while True:
    print("0 - O que deseja fazer?")
    print("1 - Mover")
    print("2 - Pegar item")
    print("3 - Ver inventário")
    print("5 - Salvar jogo")
    print("6 - Carregar jogo")
    print("7 - Sair")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        jogador.sala_atual.listar_saidas()
        direcao = input("Qual direção? ").lower()
        jogador.mover(direcao)
        
    elif opcao == "2":
        nome_item = input("Qual item deseja pegar? ")
        jogador.pegar_item(nome_item)

    elif opcao == "3":
        jogador.exibir_inventario()

    elif opcao == "5":
        try:
            arquivo_save = open("savegame.json", "w", encoding="utf-8")
            dados = {
                "nome": jogador.nome,
                "sala": jogador.sala_atual.id,
                "inventario": [{"id": i.id, "nome": i.nome, "descricao": i.descricao} for i in jogador.inventario]
            }
            json.dump(dados, arquivo_save, ensure_ascii=False, indent=4)
            arquivo_save.close()
            print("Jogo salvo com sucesso!")
        except:
            print("Erro ao salvar o jogo.")

    elif opcao == "6":
        try:
            arquivo_save = open("savegame.json", "r", encoding="utf-8")
            dados = json.load(arquivo_save)
            arquivo_save.close()
            
            jogador.nome = dados["nome"]
            jogador.sala_atual = salas[dados["sala"]]
            
            jogador.inventario = []
            for item_dado in dados["inventario"]:
                item_obj = Item(item_dado["id"], item_dado["nome"], item_dado["descricao"])
                jogador.inventario.append(item_obj)
                
                for sala in salas.values():
                    sala.itens = [i for i in sala.itens if i.id != item_obj.id]

            print("Jogo carregado com sucesso!")
            jogador.sala_atual.exibir_descricao()
            jogador.sala_atual.listar_saidas()
        except FileNotFoundError:
            print("Arquivo de save não encontrado.")

    elif opcao == "7":
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida.")