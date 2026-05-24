from utils import titulo
from tarefas import cadastrar_livro, listar_livros, buscar_livro, atualizar_status, concluir_livro, deletar_livro

def menu():
    titulo()
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Editar status do livro")
    print("5 - Concluir livro")
    print("6 - Excluir livro")
    print("7 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            atualizar_status()
        elif opcao == "5":
            concluir_livro()
        elif opcao == "6":
            deletar_livro()
        elif opcao == "7":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
