from classes.Conta import Conta

class BancoLista:
    lista_bancos = []

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