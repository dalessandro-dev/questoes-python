from classes.Banco import Banco

class BancoDoBrasil(Banco):
    def __init__(self):
        super().__init__("Banco do Brasil", "Brasil")