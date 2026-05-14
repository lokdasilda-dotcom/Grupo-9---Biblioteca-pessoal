# biblioteca pessoal
biblioteca = {}

def adicionar():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    biblioteca[titulo] = autor
    print("Livro adicionado com sucesso!")

def estante():
    if biblioteca:
            print("Sua estante de livro")
            print("-" * 30)
    for titulo, autor in biblioteca.items():
            print(f"{titulo} - {autor}")
            print("-" * 30)

def pesquisar():
    titulo = input("Digite o título do livro que deseja pesquisar: ")
    if titulo in biblioteca:
        print("-" * 30)
        print(f"{titulo} - Autor: {biblioteca[titulo]}")
        print("-" * 30)

def deletar():
    titulo = input("Digite o título do livro que deseja deletar: ")
    if titulo in biblioteca:
        del biblioteca [titulo]
        print("-" * 30)
        print("Livro deletado com sucesso!")
        print("-" * 30)
    else:
        print("-" * 30)
        print("Livro não encontrado na biblioteca.")
        print("-" * 30)


def menu():
    while True:
        print("1. Adicionar livro")
        print("2. Ver estante de livros")
        print("3. Pesquisar livro por título")
        print("4. Deletar livro por título")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar()
        elif escolha == "2":
            estante()
        elif escolha == "3":
            pesquisar()
        elif escolha == "4":
            deletar()
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")