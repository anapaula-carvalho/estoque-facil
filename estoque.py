produtos = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade inicial: "))
    minimo = int(input("Quantidade mínima: "))

    produtos.append({
        "nome": nome,
        "quantidade": quantidade,
        "minimo": minimo
    })

    print("Produto cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"{produto['nome']} - Quantidade: {produto['quantidade']}")

def verificar_estoque():
    for produto in produtos:
        if produto["quantidade"] <= produto["minimo"]:
            print(f"ALERTA: Estoque baixo - {produto['nome']}")

def registrar_saida():
    nome = input("Nome do produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            quantidade = int(input("Quantidade de saída: "))

            if quantidade <= 0:
                print("Informe uma quantidade válida.")
            elif quantidade <= produto["quantidade"]:
                produto["quantidade"] -= quantidade
                print("Saída registrada com sucesso!")
            else:
                print("Estoque insuficiente!")

            return

    print("Produto não encontrado.")

def menu():
    while True:
        print("\n===== ESTOQUE FÁCIL =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Verificar estoque")
        print("4 - Registrar saída")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            verificar_estoque()
        elif opcao == "4":
            registrar_saida()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

menu()
