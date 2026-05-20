from dados import livros, fila_lendo, pilha_concluidos, em_andamento, status, prioridades
from utils import linha

def escolher_opcao(titulo, opcoes):
    while True:
        print(f"\n{titulo}")
        for indice, opcao in enumerate(opcoes, start=1):
            print(f"{indice} - {opcao.capitalize()}")

        escolha = input("Digite a opção: ").strip()

        if escolha.isdigit():
            posicao = int(escolha) - 1
            if 0 <= posicao < len(opcoes):
                return opcoes[posicao]

        print("Opção inválida. Tente novamente.")

def encontrar_livro(busca):
    busca = busca.strip().lower()

    if not busca:
        return []

    encontrados = []

    for livro in livros:
        titulo = livro["titulo"].lower()
        autor = livro["autor"].lower()

        if busca in titulo or busca in autor:
            encontrados.append(livro)

    return encontrados

def atualizar_listas_de_status(livro):
    if livro in fila_lendo:
        fila_lendo.remove(livro)
    if livro in em_andamento:
        em_andamento.remove(livro)
    if livro in pilha_concluidos:
        pilha_concluidos.remove(livro)

    if livro["status"] == "a ler":
        fila_lendo.append(livro)
    elif livro["status"] == "lendo":
        em_andamento.append(livro)
    elif livro["status"] == "concluído":
        pilha_concluidos.append(livro)

def cadastrar_livro():
    titulo = input("Título do livro: ").strip()

    if not titulo:
        print("O título não pode ficar vazio.")
        return

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            print("Livro já cadastrado.")
            return

    autor = input("Autor do livro: ").strip()
    genero = input("Gênero do livro: ").strip()
    status_escolhido = escolher_opcao("Escolha o status:", status)
    prioridade = escolher_opcao("Escolha a prioridade:", prioridades)

    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "status": status_escolhido,
        "prioridade": prioridade,
    }

    livros.append(livro)
    atualizar_listas_de_status(livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\n===== LISTA DE LIVROS =====")
    for livro in livros:
        linha()
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Status: {livro['status']}")
        print(f"Prioridade: {livro['prioridade']}")
    linha()

def buscar_livro():
    busca = input("Digite o nome do livro ou autor: ").strip()
    encontrados = encontrar_livro(busca)

    if not encontrados:
        print("Livro não encontrado.")
        return

    print("\n===== RESULTADO DA BUSCA =====")
    for livro in encontrados:
        linha()
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Status: {livro['status']}")
        print(f"Prioridade: {livro['prioridade']}")
    linha()

def atualizar_status():
    busca = input("Digite o título ou autor do livro: ").strip()
    encontrados = encontrar_livro(busca)

    if not encontrados:
        print("Livro não encontrado.")
        return

    livro = encontrados[0]

    if len(encontrados) > 1:
        print("Mais de um livro encontrado. O primeiro resultado será alterado.")
        print(f"Livro selecionado: {livro['titulo']} | Autor: {livro['autor']}")

    print(f"\nStatus atual: {livro['status']}")
    novo_status = escolher_opcao("Escolha o novo status:", status)
    livro["status"] = novo_status
    atualizar_listas_de_status(livro)
    print("Status atualizado com sucesso!")

def concluir_livro():
    busca = input("Digite o título ou autor do livro que deseja concluir: ").strip()
    encontrados = encontrar_livro(busca)

    if not encontrados:
        print("Livro não encontrado.")
        return

    livro = encontrados[0]

    if len(encontrados) > 1:
        print("Mais de um livro encontrado. O primeiro resultado será concluído.")
        print(f"Livro selecionado: {livro['titulo']} | Autor: {livro['autor']}")

    livro["status"] = "concluído"
    atualizar_listas_de_status(livro)
    print("Livro concluído com sucesso!")

def deletar_livro():
    busca = input("Digite o título ou autor do livro que deseja excluir: ").strip()
    encontrados = encontrar_livro(busca)

    if not encontrados:
        print("Livro não encontrado.")
        return

    livro = encontrados[0]

    if len(encontrados) > 1:
        print("Mais de um livro encontrado. O primeiro resultado será excluído.")
        print(f"Livro selecionado: {livro['titulo']} | Autor: {livro['autor']}")

    livros.remove(livro)

    if livro in fila_lendo:
        fila_lendo.remove(livro)
    if livro in em_andamento:
        em_andamento.remove(livro)
    if livro in pilha_concluidos:
        pilha_concluidos.remove(livro)

    print("Livro removido com sucesso!")