# DeskBook

# Biblioteca pessoal
Grupo 9 -- Matheus Henrique Barros da Silva e Dhavi Francisco do vale Ferreira

# Descrição

Este projeto é um sistema de biblioteca pessoal. O sistema permite a inserção de novos livros, visualização de status e a possibilidade de excluir os livros da biblioteca

## Funcionalidades

- **Adicionar livros:** Adiciona novos livros com informações como título, autor.
- **Atualizar status:** Atualiza o status dos livros, como se ele ainda vai ser lido, estiver sendo lido ou concluido.
- **Buscar livros:** Busca livros registrados através do titluo ou nome do autor.
- **Excluir livros:** Exclui os livros registrados na biblioteca pessoal.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver o sistema.

## Explicações

- Fila: Ele esta sendo usado no código para salvar os livros que serão lidos.
- Pilha: Ele esta sendo usado no código para salvar os livros que já foram lidos.
- Tupla: Nós usamos bastante a tupla no tarefas porque não tinha muitas coisas para ser alteradas ao longo do tempo nele.
- Lista: Nossos dados são feitos com a lista já que eles sofrem alterações constante com o uso do programa

### Principais Funções

1. **`escolhor_opções()`**: Formulário para escolher qual opção no sistema.
   - Valida os campos e insere os dados no banco de dados.
   - Exibe as opções para que o usuario possa adicionar, buscar ou excluir livros.

2. **`cadastrar_livro()`**: Formulário para adicionar um novo livro ao sistema.
   - Valida os campos e insere os dados no banco de dados.
   - Exibe mensagem de livro registrado.

3. **`buscar_livro()`**: Exibe todos os livros cadastrados em um formato de lista, junto com o status atual do livro.
   - Exibe mensagem dos livros que foram registrados.

4. **`deletar_livro()`**: Formulário para excluir o livro.
   - Valida os campos e insere os dados no banco de dados.
   - Exibe mensagem de que o livro foi excluido.

## Como Executar

1. Certifique-se de ter o Python (ver 3.11) instalado em sua máquina.
2. Execute o seguinte comando:
   python main.py

# Dificuldades

- Na parte buscar livro, ele não estava conseguindo buscar o livro direito, somente se colocasse o nome exato. Fazer com que a busca fosse feita com apenas algumas letras do nome ou autor do livro
- A maior dificuldade foi fazer o tarefas, nossa primeira versão dele tinha muitos erros de lógica, onde nós seguia uma lógica para fazer uma parte do código e quando íamos para outra nós já trocavamos a logica, que foi oque aconteceu na parte de buscar os livros.
