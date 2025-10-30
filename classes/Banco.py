from classes.BancoLista import BancoLista

class Banco:
    def __init__(self, nome, pais):
        BancoLista.lista_bancos.append((nome, pais))
        self.__nome = nome
        self.__pais = pais

    def get_nome(self):
        return self.__nome
    
    def get_pais(self):
        return self.__pais