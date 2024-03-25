# Esse programa tem como objetivo simular um gerenciador de uma biblioteca

import json


# criando uma lista para armazenar os livros da biblioteca
import time

biblioteca = []

# Função para adicionar um livro na biblioteca
def adicionar_livro():
    título = input ("Digite o nome do livro")
    autor = input ("Digite o autor do livro")
    genero = input ("Digite o gênero do livro")
    ano_publicação = input ("Digite o ano de publicação do livro")
    status_emprestimo = False  # Inicialmente o livro não será emprestado

    livro = {
        "título": título,
        "autor": autor,
        "genero": genero,
        "ano_publicação": ano_publicação,
        "status_emprestimo": status_emprestimo
    }

    biblioteca.append(livro)
    print("Livro adicionado com sucesso!\n")

# Função para mostrar os livros disponiveis na biblioteca
def listar_livros():
    if not biblioteca:
        print("A biblioteca está vazia.")
    else:
        for idx, livro in enumerate(biblioteca, start=1):
            print(f"\nLivro {idx}:")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Gênero: {livro['genero']}")
            print(f"Ano de Publicação: {livro['ano_publicacao']}")
            status = "Disponível" if not livro['status_emprestimo'] else "Emprestado"
            print(f"Status: {status}")

# Função para buscar algum livro na biblioteca
def buscar_livro():
    termo = input("Digite o título ou autor do livro que deseja buscar: ")
    resultados = []

    for livro in biblioteca:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower():
            resultados.append(livro)

    if not resultados:
        print("Nenhum livro encontrado com o termo buscado.")
    else:
        print(f"\nResultados da busca por '{termo}':")
        for idx, livro in enumerate(resultados, start=1):
            print(f"\nLivro {idx}:")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Gênero: {livro['genero']}")
            print(f"Ano de Publicação: {livro['ano_publicacao']}")
            status = "Disponível" if not livro['status_emprestimo'] else "Emprestado"
            print(f"Status: {status}")

# Função para remover livros da biblioteca
def remover_livro():
    if not biblioteca:
        print("A biblioteca está vazia. Não há livros para remover.")
    else:
        titulo = input("Digite o título do livro que deseja remover: ")
        autor = input("Digite o nome do autor do livro que deseja remover: ")

        for livro in biblioteca:
            if livro['titulo'].lower() == titulo.lower() and livro['autor'].lower() == autor.lower():
                biblioteca.remove(livro)
                print("Livro removido com sucesso.")
                break
        else:
            print("Livro não encontrado na biblioteca.")

# Função para emprestar um livro
def emprestar_livro():
    if not biblioteca:
        print("A biblioteca está vazia. Não há livros para emprestar.")
    else:
        titulo = input("Digite o título do livro que deseja emprestar: ")

        for livro in biblioteca:
            if livro['titulo'].lower() == titulo.lower():
                if livro['status_emprestimo']:
                    print("Este livro já está emprestado.")
                else:
                    nome_usuario = input("Digite o nome do usuário que está pegando emprestado: ")
                    livro['status_emprestimo'] = True
                    livro['nome_usuario'] = nome_usuario
                    print("Livro emprestado com sucesso.")
                break
        else:
            print("Livro não encontrado na biblioteca.")


# Função para devolver algum livro
def devolver_livro():
    if not biblioteca:
        print("A biblioteca está vazia. Não há livros para devolver.")
    else:
        titulo = input("Digite o título do livro que deseja devolver: ")

        for livro in biblioteca:
            if livro['titulo'].lower() == titulo.lower() and livro['status_emprestimo']:
                livro['status_emprestimo'] = False
                del livro['nome_usuario']
                print("Livro devolvido com sucesso.")
                break
        else:
            print("Livro não encontrado na biblioteca ou não está emprestado.")

# Função para salvar os dados da biblioteca em um arquivo e carregar esses dados quando o programa for iniciado novamente.
def salvar_biblioteca():
    with open('biblioteca.json', 'w') as arquivo:
        json.dump(biblioteca, arquivo)
    print("Dados da biblioteca salvos com sucesso.")


def carregar_biblioteca():
    global biblioteca
    try:
        with open('biblioteca.json', 'r') as arquivo:
            biblioteca = json.load(arquivo)
        print("Dados da biblioteca carregados com sucesso.")
    except FileNotFoundError:
        print("Arquivo de dados da biblioteca não encontrado.")

while True:
    time.sleep(2)
    print("\n== MENU DA BIBLIOTECA ==")
    time.sleep(2)
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Buscar Livro")
    print("4. Remover Livro")
    print("5. Emprestar Livro")
    print("6. Devolver Livro")
    print("7. Salvar Dados")
    print("8. Carregar Dados")
    print("9. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        remover_livro()
    elif opcao == "5":
        emprestar_livro()
    elif opcao == "6":
        devolver_livro()
    elif opcao == "7":
        salvar_biblioteca()
    elif opcao == "8":
        carregar_biblioteca()
    elif opcao == "9":
        print("Encerrando o programa. Obrigado por usar a biblioteca!")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")