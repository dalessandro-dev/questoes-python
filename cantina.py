estoque_comida = {
    "sanduiche": 5,
    "bolo": 6,
    "coxinha": 8,
    "pastel": 10,
    "biscoito": 12,
    "pizza": 4,
    "tapioca": 7,
    "empada": 3,
    "pão": 9,
    "torta": 2
}

estoque_bebida = {
    "refrigerante": 10,
    "suco": 8,
    "cafe": 15,
    "agua": 20,
    "achocolatado": 6,
    "vitamina": 5,
    "cha": 9,
    "milkshake": 4,
    "energetico": 3,
    "leite": 10
}


def mostrar_estoque():
    """Mostra todos os produtos e suas quantidades."""
    print("\nEstoque de comidas:")
    for produto, quantidade in estoque_comida.items():
        print(f"{produto}: {quantidade}")
    print("\nEstoque de bebidas:")
    for produto, quantidade in estoque_bebida.items():
        print(f"{produto}: {quantidade}")


def adicionar_produto(nome, quantidade):
    """Adiciona um novo produto ao estoque ou soma à quantidade existente."""
    global estoque_comida, estoque_bebida

    tipo = input("O produto é (1) Comida ou (2) Bebida? ")

    if tipo == "1":
        estoque = estoque_comida
    elif tipo == "2":
        estoque = estoque_bebida
    else:
        print("Opção inválida.")
        return

    if nome in estoque:
        estoque[nome] += quantidade
        print(f"Quantidade atualizada. Agora há {estoque[nome]} unidades de {nome}.")
    else:
        estoque[nome] = quantidade
        print(f"Produto '{nome}' adicionado com {quantidade} unidades.")


def remover_produto(nome, quantidade):
    """Remove certa quantidade do produto (se houver o suficiente)."""
    global estoque_comida, estoque_bebida

    if nome in estoque_comida:
        estoque = estoque_comida
    elif nome in estoque_bebida:
        estoque = estoque_bebida
    else:
        print("Produto não encontrado.")
        return

    if estoque[nome] >= quantidade:
        estoque[nome] -= quantidade
        print(f"Foram removidas {quantidade} unidades de {nome}.")
    else:
        print(f"Quantidade insuficiente de {nome} no estoque.")


def consultar_produto(nome):
    """Mostra a quantidade atual de um produto específico."""
    if nome in estoque_comida:
        print(f"{nome} (comida): {estoque_comida[nome]} unidades.")
    elif nome in estoque_bebida:
        print(f"{nome} (bebida): {estoque_bebida[nome]} unidades.")
    else:
        print("Produto não encontrado.")


def repor_automatico():
    """Aumenta em 5 unidades qualquer item com quantidade menor que 3."""
    global estoque_comida, estoque_bebida
    for estoque in (estoque_comida, estoque_bebida):
        for produto in estoque:
            if estoque[produto] < 3:
                estoque[produto] += 5
                print(f"{produto} foi reposto automaticamente (+5 unidades).")


def salvar_relatorio():
    """Gera um arquivo 'estoque.txt' com os produtos e quantidades finais."""
    global estoque_comida, estoque_bebida

    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Relatório Final do Estoque\n\n")

        arquivo.write("Estoque de Comidas:\n")
        for produto, quantidade in estoque_comida.items():
            arquivo.write(f"{produto}: {quantidade}\n")

        arquivo.write("\nEstoque de Bebidas:\n")
        for produto, quantidade in estoque_bebida.items():
            arquivo.write(f"{produto}: {quantidade}\n")

        arquivo.write("\nRelatório gerado com sucesso.\n")

    print("Relatório salvo no arquivo 'estoque.txt'.")


def menu():
    """Menu principal do sistema."""
    while True:
        print("""
Menu Principal
1. Mostrar estoque
2. Adicionar produto
3. Remover produto
4. Consultar produto
5. Repor automático
6. Sair e salvar relatório
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            nome = input("Nome do produto: ").lower()
            quantidade = int(input("Quantidade a adicionar: "))
            adicionar_produto(nome, quantidade)
        elif opcao == "3":
            nome = input("Nome do produto: ").lower()
            quantidade = int(input("Quantidade a remover: "))
            remover_produto(nome, quantidade)
        elif opcao == "4":
            nome = input("Nome do produto: ").lower()
            consultar_produto(nome)
        elif opcao == "5":
            repor_automatico()
        elif opcao == "6":
            salvar_relatorio()
            print("Saindo do sistema. Relatório salvo.")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()
