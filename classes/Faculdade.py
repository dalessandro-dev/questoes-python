from abc import ABC

class Faculdade(ABC):
    campus = []

    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

    def info(self):
        return f"A Faculdade {self.nome} está localizada em {self.estado}."

    def buscarCampus(self, codigo):
        """Busca um campus pelo código e retorna o objeto Campus"""
        for campus in Faculdade.campus:
            if campus.codigo == codigo:
                return campus
        return None

    def criarCampus(self, campus_obj):
        """Adiciona um novo campus à lista"""
        for c in Faculdade.campus:
            if c.codigo == campus_obj.codigo:
                print(f"Erro: Campus com código '{campus_obj.codigo}' já existe.")
                return False
        
        Faculdade.campus.append(campus_obj)
        return True

    def removerCampus(self, codigo):
        """Remove um campus pelo código"""
        for c in Faculdade.campus:
            if c.codigo == codigo:
                Faculdade.campus.remove(c)
                return True
        return False
    
    def atualizarCampus(self, campus):
        """Atualiza as informações de um campus existente"""
        for c in Faculdade.campus:
            if c.codigo == campus.codigo:
                c.nome = campus.nome
                c.coordenador = campus.coordenador
                c.cep = campus.cep
                return True
        return False
    
    def listarCampus(self):
        """Retorna a lista de todos os campus"""
        return Faculdade.campus