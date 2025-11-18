class Curso:
    def __init__(self, nome, duracao, tipo, modalidade):
        self.nome = nome
        self.duracao = duracao
        self.tipo = tipo
        self.modalidade = modalidade

    def __str__(self):
        return f"[Curso] {self.nome} (Tipo: {self.tipo}, Modalidade: {self.modalidade}, Duração: {self.duracao})"
