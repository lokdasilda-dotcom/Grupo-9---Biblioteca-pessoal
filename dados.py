# Listas principais do sistema
livros = []  # Lista para armazenar todos os livros da biblioteca
fila_lendo = []  # FIFO/FILA - livros que serão lidos
pilha_concluidos = []  # LIFO/PILHA - livros concluídos
em_andamento = []  # Lista de livros que estão sendo lidos

status = ("a ler", "lendo", "concluído")
prioridades = ("baixa", "média", "alta")
