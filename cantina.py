estoque_comida = {"pastel": 10, "sanduíche": 8, "recheado": 2, "cachorro-quente": 1, "batata frita": 11, "maçã": 25, "lasanha": 12, "coxinha": 5, "bolo": 6, "tapioca": 1 }
estoque_bebida = {"suco de caju": 10, "suco de manga": 10, "suco de maracujá": 4, "refrigerante": 2, "suco de goiaba": 5, "iorgute": 23, "água": 4, "vitamina de abacaxi": 5, "água de coco": 4, "achocolatado": 1}

def mostrar_estoque():
  print("Estoque de comidas:\n")
  for item, quantidade in estoque_comida.items():
    print(f"{item}: {quantidade}")

  print("\nEstoque de bebidas:\n")
  for item, quantidade in estoque_bebida.items():
    print(f"{item}: {quantidade}")



def adicionar_produto(alimento, quantidade):
    while True:
        print("""
1. Comida
2. Bebida""")

        try:
            opcao = int(input("\nDigite a opção do tipo do produto: "))          
            if (not opcao == 1) and (not opcao == 2):
                print("Opção inválida. Tente novamente")
                continue
            break
        except:
            print("Opção inválida. Tente novamente.")
            continue
           
    if opcao == 1:
        estoque_comida[alimento] = quantidade

        print("A comida foi adicionada com sucesso.")
    elif opcao == 2:
        estoque_bebida[alimento] = quantidade

        print("A bebida foi adicionada com sucesso.")
    else:
       print("Erro")



def remover_produto(alimento):
    while True:
        print("""
1. Remover comida
2. Remover bebida""")

        try:
            opcao = int(input("\nDigite uma das opções: "))        
            if (not opcao == 1) and (not opcao == 2):
                print("Opção inválida. Tente novamente")
                continue
            break
        except:
            print("Opção inválida. Tente novamente.")
            continue
         
    if opcao == 1:
        if alimento in estoque_comida:
            del estoque_comida[alimento]
            print("O alimento foi removido com sucesso.")
        else:
            print("O alimento não existe.")
    elif opcao == 2:
        if alimento in estoque_bebida:
            del estoque_bebida[alimento]
            print("A bebida foi removida com sucesso.")
        else:
            print("A bebida não existe.")
    else:
       print("Erro")



def consultar_produto(nome):
    if nome in estoque_comida:
        print(f"A comida '{nome}' possui em estoque '{estoque_comida[nome]} unidades.'")
    elif nome in estoque_bebida:
        print(f"A bebida '{nome}' possui em estoque '{estoque_bebida[nome]} unidades.'")
    else:
        print("O alimento informado não existe.")



def repor_automatico():
    for item, quantidade in estoque_comida.items():
        if quantidade < 3:
            estoque_comida[item] += 5
    
    for item, quantidade in estoque_bebida.items():
        if quantidade < 3:
            estoque_bebida[item] += 5

    print("O estoque foi recarregado com sucesso.")



def salvar_relatorio():
    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Relatório Final do Estoque\n")

        arquivo.write("Estoque de Comidas:\n")
        for item, quantidade in estoque_comida.items():
            arquivo.write(f"{item}: {quantidade}\n")

        arquivo.write("\nEstoque de Bebidas:\n")
        for item, quantidade in estoque_bebida.items():
            arquivo.write(f"{item}: {quantidade}\n")

    print("\nRelatório gerado com sucesso.\n")



def menu():
    while True:
        print("""
CANTINA
              
1. Adicionar um novo produto
2. Remover um produto
3. Consultar um produto
4. Mostrar todos os produtos
5. Repor estoque
6. Salvar relatório e sair""")

        try:
            opcao = int(input("\nDigite uma opção: "))
        except:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == 1:
            alimento = input("Digite o nome do alimento que deseja adicionar: ")

            while True:
                try:
                    quantidade = int(input("Digite a quantidade do alimento: "))

                    adicionar_produto(alimento, quantidade)

                    break
                except:
                    print("Quantidade inválida. Tente novamente.")     
        elif opcao == 2:
            alimento = input("Digite o nome do alimento que deseja remover: ")
            
            remover_produto(alimento)
        elif opcao == 3:
            alimento = input("Digite o nome do alimento que deseja consultar: ")

            consultar_produto(alimento)
        elif opcao == 4:
            mostrar_estoque()
        elif opcao == 5:
            repor_automatico()
        elif opcao == 6:
            salvar_relatorio()

            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

