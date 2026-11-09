produtos = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade inicial: "))
    minimo = int(input("Quantidade mínima: "))

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "minimo": minimo
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"Produto: {produto['nome']} | "
            f"Quantidade: {produto['quantidade']}"
        )

def verificar_estoque():
    for produto in produtos:
        if produto["quantidade"] <= produto["minimo"]:
            print(f"ALERTA: Estoque baixo - {produto['nome']}")

def menu():
    while True:
        print("\n===== ESTOQUE FÁCIL =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Verificar estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            verificar_estoque()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

menu()
