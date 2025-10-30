from abc import ABC
    
class Conta(ABC):
    _contador_numero = 0
    
    def __init__(self, titular, cpf, tipoDeConta, banco):
        Conta._contador_numero += 1
        self._titular = titular
        self._numero = Conta._contador_numero
        self._cpf = cpf
        self._tipoDeConta = tipoDeConta
        self._saldo = 0
        self._banco = banco

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