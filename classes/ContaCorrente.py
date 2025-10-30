from classes.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, cpf, banco):
        super().__init__(titular, cpf, "corrente", banco)
