from abc import ABC

class Conta(ABC):
    _contador_numero = 0
    
    def __init__(self, titular, cpf, tipoDeConta):
        Conta._contador_numero += 1
        self._titular = titular
        self._numero = Conta._contador_numero
        self._cpf = cpf
        self._tipoDeConta = tipoDeConta
        self._saldo = 0

    def get_numero(self):
        return self._numero
    
    def get_saldo(self):
        return self._saldo
    
    def creditar(self, valor):
        self._saldo += valor
        self.get_saldo()

    def debitar(self, valor):
        if self._saldo < valor:
            print("Saldo insufiente.")
        
        self._saldo -= valor
        self.get_saldo()

class ContaCorrente(Conta):
    def __init__(self, titular, cpf):
        super().__init__(titular, cpf, "corrente")


class Banco:
    def __init__(self):
        self.contas = [None] * 100
        self.indice = 0

    def cadastrar(self, conta: Conta):
        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):
        i = 0
        achou = False

        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1

        if achou is True:
            return self.contas[i]
        else:
            return None
        
    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)

        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente!")
    
    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)

        if conta:
            conta.creditar(valor)
        else:
            print("Conta Inexistente!")

    def transferir(self, origem, destino, valor):
        contaRemetente = self.procurar_conta(origem)
        contaDestinatario = self.procurar_conta(destino)

        if not contaRemetente:
            print("A conta de origem não existe!")
        elif not contaDestinatario:
            print("A conta de destino não existe!")
        
        contaRemetente.debitar(valor)
        contaDestinatario.creditar(valor)
    
    def consultar_saldo(self, numero):
        conta = self.procurar_conta(numero)

        if conta:
            print(conta.get_saldo())
        else:
            print("Conta inexistente!")
    
def main():
    banco = Banco()

    while True:
        print("=== Bem-vindo ao banco ===")
        opcao = input("""
1. Cadastrar uma conta
2. Procurar uma conta
3. Retirar uma quantia do saldo da conta
4. Adicionar uma quantia ao saldo da conta
5. Transferir o dinheiro
6. Consultar saldo da conta
7. Sair

\n-> Digite o número da ação que deseja realizar: """)

        if opcao == "1":
            titular = input("\n-> Digite o nome do titular da conta: ")
            cpf = input("\n-> Digite o CPF do titular da conta: ")

            banco.cadastrar(ContaCorrente(titular, cpf))
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
            print("Saindo...")
            break
        else:
            print("\nDigite uma opção válida!")

main()