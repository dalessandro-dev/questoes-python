from classes.BancoLista import BancoLista
from classes.ContaCorrente import ContaCorrente
from classes.Nubank import Nubank
from classes.BancoDoBrasil import BancoDoBrasil

def main():
    banco = BancoLista()
    nubank = Nubank()
    bancoDoBrasil = BancoDoBrasil()

    while True:
        print("=== Bem-vindo ao banco ===")
        opcao = input("""
1. Cadastrar uma conta
2. Procurar uma conta
3. Retirar uma quantia do saldo da conta
4. Adicionar uma quantia ao saldo da conta
5. Transferir o dinheiro
6. Consultar saldo da conta
7. Ver opções de bancos
8. Sair

-> Digite o número da ação que deseja realizar: """)

        if opcao == "1":
            titular = input("\n-> Digite o nome do titular da conta: ")
            cpf = input("\n-> Digite o CPF do titular da conta: ")
            bancoConta = input(f"""
1. Nubank
2. Banco do Brasil

-> Digite a opção do banco que deseja utilizar: """)

            if bancoConta == "1":
                banco.cadastrar(ContaCorrente(titular, cpf, nubank))
            elif bancoConta == "2":
                banco.cadastrar(ContaCorrente(titular, cpf, bancoDoBrasil))
        elif opcao == "2":
            numero = int(input("\n-> Digite o número da conta: "))

            conta = banco.procurar_conta(numero)

            if conta:
                print(conta)
            else:
                print("Conta inexistente!")
        elif opcao == "3":
            numero = int(input("\n-> Digite o numero da conta: "))
            valor = float(input("\n-> Digite o valor que deseja retirar: "))

            banco.debitar(numero, valor)
        elif opcao == "4":
            numero = int(input("\n-> Digite o numero da conta: "))
            valor = float(input("\n-> Digite o valor que deseja adicionar: "))

            banco.creditar(numero, valor)
        elif opcao == "5":
            numeroRemetente = int(input("\n-> Digite o número da conta de origem: "))
            numeroDestinatario = int(input("\n-> Digite o número da conta de destino: "))
            valor = float(input("\n-> Digite o valor que deseja transferir: "))

            banco.transferir(numeroRemetente, numeroDestinatario, valor)
        elif opcao == "6":
            numero = int(input("\n-> Digite o número da conta: "))

            banco.consultar_saldo(numero)
        elif opcao == "7":
            print(banco.lista_bancos)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("\nDigite uma opção válida!")

main()