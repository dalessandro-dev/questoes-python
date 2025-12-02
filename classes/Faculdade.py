from abc import ABC

class Faculdade(ABC):
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado
        self.campus = []

    def info(self):
        return f"A Faculdade {self.nome} está localizada em {self.estado}."

    def adicionarCampus(self, campus_obj):
        for c in self.campus:
            if c.nome == campus_obj.nome:
                return f"Campus '{campus_obj.nome}' já existe."
        
        self.campus.append(campus_obj)
        return f"Campus '{campus_obj.nome}' adicionado."

    def removerCampus(self, nome_campus):
        for c in self.campus:
            if c.nome == nome_campus:
                self.campus.remove(c)
                return f"Campus '{nome_campus}' removido."
        return f"Campus '{nome_campus}' não encontrado."
    
    def atualizarCampus(self, nomeAntigo, nomeNovo):
        for c in self.campus:
            if c.nome == nomeAntigo:
                c.nome = nomeNovo
                return True
        return False
    
    def listarCampus(self):
        return self.campus

class UFC(Faculdade):
    def __init__(self):
        super().__init__(nome="Universidade Federal do Ceará", estado="CE")